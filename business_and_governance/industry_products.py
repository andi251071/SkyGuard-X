# INDUSTRY-SPECIFIC DATA PRODUCTS 
from datetime import datetime 
import random 
 
class IndustryDataProducts: 
    def __init__(self): 
        self.products = { 
            'agriculture': {'price': 299, 'name': 'Crop Health Analytics'}, 
            'security': {'price': 599, 'name': 'Perimeter Monitoring'}, 
            'construction': {'price': 399, 'name': 'Site Progress Tracking'}, 
            'logistics': {'price': 499, 'name': 'Delivery Route Optimization'} 
        } 
 
    def get_agriculture_data(self): 
        return { 
            'crop_health_score': round(random.uniform(0.5, 1.0), 3), 
            'ndvi_index': round(random.uniform(0.1, 0.9), 3), 
            'pest_risk_level': random.choice(['low', 'medium', 'high']), 
            'yield_prediction': round(random.uniform(5, 15), 2), 
            'irrigation_recommendation': round(random.uniform(10, 50), 2), 
            'timestamp': datetime.now().isoformat() 
        } 
 
    def get_security_data(self): 
        return { 
            'intrusion_detected': random.choice([True, False]), 
            'threat_level': random.choice(['low', 'medium', 'high', 'critical']), 
            'object_count': random.randint(0, 20), 
            'response_time': round(random.uniform(30, 300), 2), 
            'coverage_area': round(random.uniform(1, 100), 2), 
            'timestamp': datetime.now().isoformat() 
        } 
 
    def get_construction_data(self): 
        return { 
            'progress_percentage': round(random.uniform(0, 100), 2), 
            'equipment_count': random.randint(5, 50), 
            'safety_compliance': round(random.uniform(80, 100), 2), 
            'material_delivery_status': random.choice(['on_time', 'delayed', 'early']), 
            'worker_productivity': round(random.uniform(60, 95), 2), 
            'timestamp': datetime.now().isoformat() 
        } 
 
    def get_logistics_data(self): 
        return { 
            'delivery_efficiency': round(random.uniform(70, 98), 2), 
            'route_optimization_score': round(random.uniform(80, 99), 2), 
            'fuel_consumption': round(random.uniform(8, 15), 2), 
            'delivery_time_variance': round(random.uniform(-30, 30), 2), 
            'vehicle_utilization': round(random.uniform(60, 95), 2), 
            'timestamp': datetime.now().isoformat() 
        } 
