from rest_framework import serializers
from .models import Drone, Mission, ThreatAlert

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = "__all__"

class MissionSerializer(serializers.ModelSerializer):
    assigned_drones = DroneSerializer(many=True, read_only=True)
    
    class Meta:
        model = Mission
        fields = "__all__"

class ThreatAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreatAlert
        fields = "__all__"
