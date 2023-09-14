from django.contrib import admin

from .models import Posts, Votes

# Register your models here.
admin.site.register(Posts)
admin.site.register(Votes)
