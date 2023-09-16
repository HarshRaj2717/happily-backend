from django.contrib import admin

from .models import Professionals, Appointments, Chats

# Register your models here.
admin.site.register(Professionals)
admin.site.register(Appointments)
admin.site.register(Chats)
