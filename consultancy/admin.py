from django.contrib import admin

from .models import Appointments, Chats, Professionals

# Register your models here.
admin.site.register(Professionals)
admin.site.register(Appointments)
admin.site.register(Chats)
