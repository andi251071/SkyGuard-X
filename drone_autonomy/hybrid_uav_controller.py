class HybridUAVController: 
    def __init__(self, drone_id="SGX-001"): 
        self.drone_id = drone_id 
        self.connected = False 
        self.battery = 100 
        print("Drone", drone_id, "initialized") 
 
    def connect(self): 
        self.connected = True 
        return {"status": "connected", "drone_id": self.drone_id} 
 
    def start_mission(self, mission_type="surveillance"): 
        return {"status": "mission_started", "type": mission_type, "battery": self.battery} 
 
    def get_status(self): 
        return {"drone_id": self.drone_id, "connected": self.connected, "battery": self.battery} 
