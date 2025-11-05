import threading  
import time  
from datetime import datetime  
  
class RealTimeProcessor:  
    def __init__(self):  
        print("RealTime Processor Started!")  
  
    def stream_drone_data(self, drone_id, data):  
        message = {  
            "drone_id": drone_id,  
            "data": data,  
            "timestamp": datetime.now().isoformat()  
        }  
        print(f"?? REAL-TIME: {message}")  
        return True  
  
    def start_background_processor(self):  
        def processor_loop():  
            while True:  
                time.sleep(3)  
                self.stream_drone_data(1, {"battery": 85, "status": "active"})  
  
        thread = threading.Thread(target=processor_loop, daemon=True)  
        thread.start()  
