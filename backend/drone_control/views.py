from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Drone, Mission, ThreatAlert
from .serializers import DroneSerializer, MissionSerializer, ThreatAlertSerializer

class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    
    @action(detail=False, methods=["get"])
    def active_drones(self, request):
        active_drones = Drone.objects.filter(status="ACTIVE")
        serializer = self.get_serializer(active_drones, many=True)
        return Response(serializer.data)

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class ThreatAlertViewSet(viewsets.ModelViewSet):
    queryset = ThreatAlert.objects.filter(is_active=True)
    serializer_class = ThreatAlertSerializer
