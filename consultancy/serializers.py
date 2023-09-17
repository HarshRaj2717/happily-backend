from rest_framework import serializers

from .models import Professionals, Chats, Appointments


class ProfessionalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionals
        fields = '__all__'
