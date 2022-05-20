from rest_framework import serializers

from .models import AirPlane
from .services import calculate_fuel_consumption
from .services import calculate_fuel_tank


class AirPlaneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    fuel_tank = serializers.SerializerMethodField()
    fuel_consumption_per_minute = serializers.SerializerMethodField()
    max_time_for_fly = serializers.SerializerMethodField()

    class Meta:
        model = AirPlane
        fields = ['id', 'passenger_capacity', 'fuel_tank', 'fuel_consumption_per_minute', 'max_time_for_fly']

    def get_fuel_tank(self, obj):
        return calculate_fuel_tank(obj.id)

    def get_fuel_consumption_per_minute(self, obj):
        return calculate_fuel_consumption(obj.id, obj.passenger_capacity)

    def get_max_time_for_fly(self, obj):
        return calculate_fuel_tank(obj.id) / calculate_fuel_consumption(
            obj.id,
            obj.passenger_capacity
        )
