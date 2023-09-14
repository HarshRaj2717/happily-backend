from django.contrib import admin

from .models import Comments, Posts, Votes

# Register your models here.
admin.site.register(Posts)
admin.site.register(Votes)
admin.site.register(Comments)
