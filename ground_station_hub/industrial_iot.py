# INDUSTRIAL IOT SENSOR INTEGRATION 
import time 
import json 
from datetime import datetime 
 
class IndustrialIoT: 
    def __init__(self): 
        self.sensors = {} 
        print("Industrial IoT System Initialized") 
 
    def register_sensor(self, sensor_id, sensor_type, location): 
        self.sensors[sensor_id] = { 
            'type': sensor_type, 
            'location': location, 
            'status': 'active', 
            'last_read': None 
        } 
        return f"Sensor {sensor_id} registered" 
 
    def read_sensor_data(self, sensor_id): 
        # Simulate industrial sensor readings 
        import random 
        sensor = self.sensors.get(sensor_id) 
        if sensor: 
            sensor_type = sensor['type'] 
            if sensor_type == 'temperature': 
                value = round(random.uniform(15.0, 45.0), 2) 
            elif sensor_type == 'vibration': 
                value = round(random.uniform(0.1, 5.0), 3) 
            elif sensor_type == 'acoustic': 
                value = round(random.uniform(30.0, 120.0), 1) 
            else: 
                value = round(random.uniform(0, 100), 2) 
 
            sensor_data = { 
                'sensor_id': sensor_id, 
                'type': sensor_type, 
                'value': value, 
                'unit': self._get_unit(sensor_type), 
                'timestamp': datetime.now().isoformat(), 
                'location': sensor['location'] 
            } 
            sensor['last_read'] = datetime.now() 
            return sensor_data 
        return None 
 
    def _get_unit(self, sensor_type): 
        units = { 
            'temperature': 'øC', 
            'vibration': 'g', 
            'acoustic': 'dB', 
            'pressure': 'kPa', 
            'humidity': '%' 
        } 
        return units.get(sensor_type, 'units') 
 
    def get_equipment_health(self): 
        # Predictive maintenance simulation 
        health_data = {} 
        for sensor_id, sensor in self.sensors.items(): 
            reading = self.read_sensor_data(sensor_id) 
            if reading: 
                # Simple health algorithm 
                if sensor['type'] == 'vibration' and reading['value'] 
                    health_status = 'warning' 
                elif sensor['type'] == 'temperature' and reading['value'] 
                    health_status = 'critical' 
                else: 
                    health_status = 'normal' 
 
                health_data[sensor_id] = { 
                    'status': health_status, 
                    'value': reading['value'], 
                    'timestamp': reading['timestamp'] 
                } 
        return health_data 
