from rest_framework.decorators import api_view
from rest_framework.response import Response

from authenticator.models import Users

from .models import Appointments, Chats, Professionals
from .serializers import (AppointmentsSerializer, ChatsSerializer,
                          ProfessionalsSerializer)

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
def all_appointments(request, user_key):
    try:
        user = Users.objects.get(api_token=user_key)
        appointments = Appointments.objects.filter(user=user)
        serializer = AppointmentsSerializer(appointments, many=True)
        if serializer.data == []:
            try:
                appointments = Appointments.objects.filter(
                    professional=Professionals.objects.get(email=user))
                serializer = AppointmentsSerializer(appointments, many=True)
            except:
                return Response({
                    "success": 1,
                    "appointments": []
                })
        return Response({
            "success": 1,
            "appointments": serializer.data
        })
    except:
        return Response({"success": 0})


@api_view(["GET", "POST"])
def chat(request, user_key, appointment_id):
    if request.method == "GET":
        try:
            appointment = Appointments.objects.get(id=appointment_id)
            user = Users.objects.get(api_token=user_key)
            assert appointment.user == user or appointment.professional == Professionals.objects.get(
                email=user)
            all_chats = Chats.objects.filter(appointment_id=appointment)
            serializer = ChatsSerializer(all_chats, many=True)
            return Response({
                "success": 1,
                "chats": serializer.data
            })
        except:
            return Response({"success": 0})
    elif request.method == "POST":
        try:
            data = request.data
            appointment = Appointments.objects.get(id=appointment_id)
            user = Users.objects.get(api_token=user_key)
            assert appointment.user == user or appointment.professional == Professionals.objects.get(
                email=user)
            assert data['content'].strip() != ""
            new_chat = Chats.objects.create(
                appointment_id=appointment,
                sender="user" if user.verified_as == "user" else "professional",
                content=data['content'].strip()
            )
            new_chat.save()
            all_chats = Chats.objects.filter(appointment_id=appointment)
            serializer = ChatsSerializer(all_chats, many=True)
            return Response({
                "success": 1,
                "chats": serializer.data
            })
        except:
            return Response({"success": 0})
