from random import randint

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import helpers
from .models import Users

# Create your views here.


@api_view(['GET'])
def register_user(request):
    EMAIL = request.GET.get('email')
    PASSWORD = request.GET.get('password')
    VERIFICATION_CODE = request.GET.get('code')

    # In case an verification_code is provided
    if VERIFICATION_CODE != None:
        try:
            # Checking user status in existing database
            cur_user = Users.objects.get(email=EMAIL)
            cur_user_status = cur_user.user_status()
            if cur_user_status == 0:
                return Response({
                    'success': 0,
                    'message': 'Sorry, the user has been blocked or deleted.',
                    'redirect': None,
                })
            elif cur_user_status == 1 or cur_user_status == 2:
                if cur_user.match_verification_code(VERIFICATION_CODE) or cur_user_status == 2:
                    return Response({
                        'success': 1,
                        'message': 'Account Verified.',
                        'redirect': '/',
                        'api_token': cur_user.api_token,
                    })
                else:
                    return Response({
                        'success': 0,
                        'message': 'Incorrect verification code entered!',
                        'redirect': None,
                    })
            else:
                return Response({
                    'success': 0,
                    'message': 'Unknown Exception Occurred!',
                    'redirect': None,
                })
        except Users.DoesNotExist:
            return Response({
                'success': 0,
                'message': 'Unknown Exception Occurred!',
                'redirect': None,
            })

    # Checking if both email & password not are given
    if EMAIL == None or EMAIL.strip() == "" or PASSWORD == None or PASSWORD.strip() == "":
        return Response({
            'success': 0,
            'message': 'Please provide both email & password.',
            'redirect': None,
        })

    PASSWORD = helpers.generate_hash(PASSWORD)
    api_token = helpers.generate_hash(
        str(EMAIL + PASSWORD + str(randint(1, 20))))

    try:
        # Checking user status in existing database
        cur_user = Users.objects.get(email=EMAIL)
        cur_user_status = cur_user.user_status()
        if cur_user_status == 0:
            return Response({
                'success': 0,
                'message': 'Sorry, the user has been blocked or deleted.',
                'redirect': None,
            })
        elif cur_user_status == 1:
            return Response({
                'success': 1,
                'message': 'Verification Code Sent.',
                'redirect': '/verify',
            })
        elif cur_user_status == 2:
            return Response({
                'success': 0,
                'message': 'User already exists! Please Login.',
                'redirect': '/login',
            })
        else:
            return Response({
                'success': 0,
                'message': 'Unknown Exception Occurred!',
                'redirect': None,
            })
    except Users.DoesNotExist:
        cur_user = Users(
            email=EMAIL,
            password=PASSWORD,
            api_token=api_token
        )

    if cur_user.is_email_disposable():
        return Response({
            'success': 0,
            'message': 'Disposable email detected. Please use a different mailing id.',
            'redirect': None,
        })

    if cur_user.send_verification_code():
        return Response({
            'success': 1,
            'message': 'Verification Code Sent.',
            'redirect': '/verify',
        })
    else:
        return Response({
            'success': 0,
            'message': 'Unknown Exception Occurred!',
            'redirect': None,
        })


@api_view(['GET'])
def login_user(request):
    EMAIL = request.GET.get('email')
    PASSWORD = request.GET.get('password')
    VERIFICATION_CODE = request.GET.get('code')

    # In case an verification_code is provided
    if VERIFICATION_CODE != None:
        try:
            # Checking user status in existing database
            cur_user = Users.objects.get(EMAIL)
            cur_user_status = cur_user.user_status()
            if cur_user_status == 0:
                return Response({
                    'success': 0,
                    'message': 'Sorry, the user has been blocked or deleted.',
                    'redirect': None,
                })
            elif cur_user_status == 1 or cur_user_status == 2:
                if cur_user.match_verification_code(VERIFICATION_CODE) or cur_user_status == 2:
                    return Response({
                        'success': 1,
                        'message': 'Account Verified.',
                        'redirect': '/',
                        'api_token': cur_user.api_token,
                    })
                else:
                    return Response({
                        'success': 0,
                        'message': 'Incorrect verification code entered!',
                        'redirect': None,
                    })
            else:
                return Response({
                    'success': 0,
                    'message': 'Unknown Exception Occurred!',
                    'redirect': None,
                })
        except Users.DoesNotExist:
            return Response({
                'success': 0,
                'message': 'Unknown Exception Occurred!',
                'redirect': None,
            })

    # Checking if both email & password are not given
    if EMAIL == None or EMAIL.strip() == "" or PASSWORD == None or PASSWORD.strip() == "":
        return Response({
            'success': 0,
            'message': 'Please provide both email & password.',
            'redirect': None,
        })

    # Checking if both email & password aren't very long in length
    if len(EMAIL.strip()) > 100 or len(PASSWORD.strip()) > 20:
        return Response({
            'success': 0,
            'message': 'Too long email or password.',
            'redirect': None,
        })

    PASSWORD = helpers.generate_hash(PASSWORD)

    try:
        # Checking user status in existing database
        cur_user = Users.objects.get(email=EMAIL)
        cur_user_status = cur_user.user_status()
        if cur_user_status == 0:
            return Response({
                'success': 0,
                'message': 'Sorry, the user has been blocked or deleted.',
                'redirect': None,
            })
        elif cur_user_status == 1:
            return Response({
                'success': 0,
                'message': 'User not verified.',
                'redirect': '/verify',
            })
        elif cur_user_status == 2:
            if cur_user.password == PASSWORD:
                return Response({
                    'success': 1,
                    'message': 'Logged in.',
                    'redirect': '/',
                    'api_token': cur_user.api_token,
                })
            else:
                return Response({
                    'success': 0,
                    'message': 'Incorrect password.',
                    'redirect': None,
                })
        else:
            return Response({
                'success': 0,
                'message': 'Unknown Exception Occurred!',
                'redirect': None,
            })
    except:
        return Response({
            'success': 0,
            'message': 'User doesn\'t exists.',
            'redirect': '/register',
        })
