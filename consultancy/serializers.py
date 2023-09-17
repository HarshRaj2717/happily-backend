from rest_framework import serializers

from .models import Appointments, Chats, Professionals


class ProfessionalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionals
        fields = '__all__'


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = '__all__'



class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = '__all__'

