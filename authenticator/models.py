import smtplib
from email.message import EmailMessage
from random import randint

import requests
from django.conf import settings
from django.db import models

from . import helpers

# Create your models here.


class Users(models.Model):
    email = models.EmailField(
        unique=True,
        primary_key=True,
    )
    password = models.CharField(max_length=65)
    api_token = models.CharField(max_length=65)
    verified = models.BooleanField(default=False)
    cur_code = models.CharField(max_length=65)
    active = models.BooleanField(default=True)
    # tier-0 == Free, 1 == Premium
    tier = models.PositiveSmallIntegerField(default=0)
    verified_as = models.TextField(
        choices=[("user", "User"), ("psychologist", "Psychologist"),
                 ("psychiatrist", "Psychiatrist"), ("ngo", "NGO/Indepent Body")],
        default="user",
    )

    def __str__(self) -> str:
        return f"{self.email} - {self.verified_as}"

    def send_verification_code(self) -> bool:
        """
        Generate a random 6-digit verification code

        Send the OTP to provided email_id

        Return the success status (True/False) after sending mail
        """
        verification_code = str(randint(100000, 999999))
        self.cur_code = helpers.generate_hash(verification_code)

        msg = EmailMessage()
        msg['Subject'] = 'Verify your Happily account!'
        msg['From'] = settings.EMAIL_ADDRESS
        msg['To'] = self.email
        msg.set_content(f'''
                        <!DOCTYPE html>
                        <html lang="en">
                        <body>
                            <p>
                            Please verify your Happily account. Here is your verification code:
                            </p>
                            <h3>{verification_code}</h3>
                            <p>
                            If you haven't attempted to register/login to
                            <a href="http://{settings.CLIENT_URL}" target="_blank" rel="noopener noreferrer"
                                >Happily</a
                            >
                            then please ignore this mail.
                            </p>
                            <hr>
                            <small>
                                <p>This is an automatically generated email; please don't reply. For any queries, contact (<a href="mailto:happily.moonandstars@gmail.com">happily.moonandstars@gmail.com</a>)</p>
                            </small>
                            <br>
                            <p>Regards:</p>
                            <p>Moon And Stars Team (Happily)</p>
                        </body>
                        </html>
                        ''', subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
            smtp.send_message(msg)

        self.save()
        return True

    def match_verification_code(self, verification_code: str) -> bool:
        """
        Match the provided otp with email_id's cur_code

        Set verified = True and cur_otp = "" for the provided email_id

        Send a mail confirming account verification to the provided email_id

        Return the match status (True/False) after sending mail
        """
        verification_code = helpers.generate_hash(verification_code)
        if verification_code == self.cur_code:
            self.cur_code = '.'
            self.verified = True
            self.save()

            msg = EmailMessage()
            msg['Subject'] = 'Happily - Account verification successful!'
            msg['From'] = settings.EMAIL_ADDRESS
            msg['To'] = self.email
            msg.set_content(f'''
                            <!DOCTYPE html>
                            <html lang="en">
                            <body>
                                <h3>
                                🎉 Account verification successful!
                                </h3>
                                <p>
                                Welcome to the Happily community ❤️.
                                </p>
                                <hr>
                                <small>
                                    <p>This is an automatically generated email; please don't reply. For any queries, contact (<a href="mailto:happily.moonandstars@gmail.com">happily.moonandstars@gmail.com</a>)</p>
                                </small>
                                <br>
                                <p>Regards:</p>
                                <p>Moon And Stars Team (Happily)</p>
                            </body>
                            </html>
                            ''', subtype='html')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
                smtp.send_message(msg)

            return True
        else:
            return False

    def is_email_disposable(self) -> bool:
        """
        Check if provided email_id is a disposable email using https://www.mailcheck.ai/
        """
        mail_check_response = requests.get(
            f'https://api.mailcheck.ai/email/{self.email}')
        if mail_check_response.status_code not in range(200, 300):
            msg = EmailMessage()
            msg['Subject'] = 'Happily - Mail verification issues...'
            msg['From'] = settings.EMAIL_ADDRESS
            msg['To'] = f"{self.email}, {settings.EMAIL_ADDRESS}"
            msg.set_content(f'''
                            <!DOCTYPE html>
                            <html lang="en">
                            <body>
                                <p>
                                Issues detected with mail verification on Happily website! All emails (disposable/non-disposable) will get disallowed from registration untill the issue is fixed.
                                </p>
                                <p>
                                mailcheck.ai reponse status code - {str(mail_check_response.status_code)}
                                </p>
                                <p>
                                Don't worry, a copy of this mail has been sent to our team, we will fix this issue as soon as possible 🤝🏻.
                                </p>
                                <hr>
                                <small>
                                    <p>This is an automatically generated email; please don't reply. For any queries, contact (<a href="mailto:happily.moonandstars@gmail.com">happily.moonandstars@gmail.com</a>)</p>
                                </small>
                                <br>
                                <p>Regards:</p>
                                <p>Moon And Stars Team (Happily)</p>
                            </body>
                            </html>
                            ''', subtype='html')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(settings.EMAIL_ADDRESS, settings.EMAIL_PASSWORD)
                smtp.send_message(msg)

            return True

        mail_check_response_json = mail_check_response.json()
        if mail_check_response_json['disposable'] == True:
            return True
        else:
            return False

    def user_status(self) -> int:
        """
        Check and return user status as:
            0 == Not-active (Deleted/Blocked),
            1 == Active & Not-verified
            2 == Active & Verified
        """
        if self.active == False:
            return 0
        if self.verified == False:
            return 1
        return 2
