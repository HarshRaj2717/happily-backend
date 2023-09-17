from django.db import models
from django.db.models import Q

# Create your models here.


class Professionals(models.Model):
    email = models.OneToOneField(
        'authenticator.Users',
        on_delete=models.CASCADE,
        limit_choices_to=Q(verified_as="psychologist") | Q(
            verified_as="psychiatrist")
    )
    description = models.TextField(null=True, blank=True)
    experience_in_years = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices=([(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        default=0
    )
    verified_as = models.TextField(
        choices=[("psychologist", "Psychologist"),
                 ("psychiatrist", "Psychiatrist")],
    )
    no_of_ratings = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    charge = models.PositiveIntegerField(default=0)
    appointment_duration_hours = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.email}"


class Appointments(models.Model):
    user = models.ForeignKey('authenticator.Users', on_delete=models.CASCADE)
    professional = models.ForeignKey(
        'consultancy.Professionals', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    fulfilled = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.id)  # type: ignore


class Chats(models.Model):
    appointment_id = models.ForeignKey(
        'consultancy.Appointments', on_delete=models.CASCADE)
    sender = models.TextField(
        choices=[("user", "user"), ("professional", "professional")], null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.id)  # type: ignore
