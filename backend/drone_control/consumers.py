import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Drone

class DroneStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send_initial_data()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        if data.get("type") == "request_update":
            await self.send_drone_status()

    async def send_initial_data(self):
        drones = await self.get_drones_data()
        await self.send(text_data=json.dumps({
            "type": "initial_data",
            "drones": drones
        }))

    async def send_drone_status(self):
        drones = await self.get_drones_data()
        await self.send(text_data=json.dumps({
            "type": "drone_status", 
            "drones": drones
        }))

    @sync_to_async
    def get_drones_data(self):
        drones = Drone.objects.all()
        return [
            {
                "id": str(drone.id),
                "name": drone.name,
                "type": drone.drone_type,
                "status": drone.status,
                "position": {
                    "lat": drone.latitude,
                    "lng": drone.longitude,
                    "alt": drone.altitude
                },
                "battery": drone.battery_level,
                "signal": drone.signal_strength
            }
            for drone in drones
        ]

class ThreatAlertConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
