from django.contrib import admin

# Register your models here.
from .models import Meeting
admin.site.register(Meeting)

from .models import Room
admin.site.register(Room)

