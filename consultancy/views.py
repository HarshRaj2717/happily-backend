from rest_framework.decorators import api_view
from rest_framework.response import Response

from authenticator.models import Users

from .models import Professionals, Appointments
from .serializers import ProfessionalsSerializer
# Create your views here.


@api_view(["GET"])
def get_professionals(request):
    try:
        professionals = Professionals.objects.filter(available=True)
        serializer = ProfessionalsSerializer(professionals, many=True)
        return Response({
            "success": 1,
            "profs": serializer.data
        })
    except:
        return Response({"success": 0})


@api_view(["GET"])
def book_appointment(request, user_key, prof_id):
    try:
        user = Users.objects.get(api_token=user_key)
        prof = Professionals.objects.get(id=prof_id)
        assert prof.available == True
        appointment = Appointments.objects.create(
            user=user,
            professional=prof,
            paid=prof.charge == 0,
        )
        appointment.save()
        return Response({
            "success": 1,
            "appointment_id": appointment.id  # type: ignore
        })
    except Exception as e:
        return Response({"success": 0, "msg": str(e)})


@api_view(["GET"])
def pay_appointment(request, user_key, appointment_id):
    try:
        # TODO payment functionality
        user = Users.objects.get(api_token=user_key)
        appointment = Appointments.objects.get(id=appointment_id)
        assert appointment.user == user
        appointment.paid = True
        appointment.save()
        return Response({
            "success": 1,
        })
    except:
        return Response({"success": 0})


@api_view(["GET"])
def all_chats(request, user_key):
    try:
        return Response({
            "success": 1,
        })
    except:
        return Response({"success": 0})


@api_view(["GET", "POST"])
def chat(request, user_key):
    if request.method == "GET":
        try:
            return Response({
                "success": 1,
            })
        except:
            return Response({"success": 0})
    elif request.method == "POST":
        try:
            return Response({
                "success": 1,
            })
        except:
            return Response({"success": 0})
