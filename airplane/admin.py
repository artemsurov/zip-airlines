from django.contrib import admin

from .models import AirPlane


@admin.register(AirPlane)
class AirPlaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger_capacity')
