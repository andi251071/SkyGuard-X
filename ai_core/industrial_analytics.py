# INDUSTRIAL DATA ANALYTICS 
import numpy as np 
import json 
from datetime import datetime, timedelta 
 
class IndustrialAnalytics: 
    def __init__(self): 
        self.data_history = {} 
        print("Industrial Analytics Engine Started") 
 
    def add_sensor_data(self, sensor_data): 
        sensor_id = sensor_data['sensor_id'] 
        if sensor_id not in self.data_history: 
            self.data_history[sensor_id] = [] 
 
        self.data_history[sensor_id].append({ 
            'value': sensor_data['value'], 
            'timestamp': sensor_data['timestamp'] 
        }) 
 
        # Keep only last 1000 readings 
        if len(self.data_history[sensor_id]) 
            self.data_history[sensor_id] = self.data_history[sensor_id][-1000:] 
 
    def calculate_trends(self, sensor_id, window=10): 
            return None 
 
        values = [entry['value'] for entry in self.data_history[sensor_id][-window:]] 
            return None 
 
        # Simple trend calculation 
        x = np.arange(len(values)) 
        y = np.array(values) 
        z = np.polyfit(x, y, 1) 
        slope = z[0] 
 
        if slope 
            trend = 'increasing' 
            trend = 'decreasing' 
        else: 
            trend = 'stable' 
 
        return { 
            'trend': trend, 
            'slope': round(slope, 4), 
            'current_value': values[-1], 
            'average': round(np.mean(values), 2), 
            'std_dev': round(np.std(values), 3) 
        } 
 
    def detect_anomalies(self, sensor_id, threshold=2): 
            return None 
 
        values = [entry['value'] for entry in self.data_history[sensor_id]] 
        mean = np.mean(values) 
        std = np.std(values) 
 
        latest_value = values[-1] 
        z_score = abs((latest_value - mean) / std) if std  else 0 
 
        is_anomaly = z_score 
 
        return { 
            'is_anomaly': is_anomaly, 
            'z_score': round(z_score, 3), 
            'value': latest_value, 
            'mean': round(mean, 2), 
            'threshold': threshold 
        } 
