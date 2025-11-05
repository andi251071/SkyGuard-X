from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DroneViewSet, MissionViewSet, ThreatAlertViewSet

router = DefaultRouter()
router.register("drones", DroneViewSet)
router.register("missions", MissionViewSet)
router.register("threats", ThreatAlertViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
