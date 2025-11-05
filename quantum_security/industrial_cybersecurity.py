from datetime import datetime 
 
class IndustrialSecurity: 
    def __init__(self): 
        self.security_events = [] 
        print("Industrial Cybersecurity System Activated") 
 
    def monitor_system_health(self, system_data): 
        # Monitor for unusual patterns 
        alerts = [] 
 
        # Check for rapid parameter changes 
        if 'vibration' in system_data and system_data['vibration'] 
            alerts.append({ 
                'level': 'HIGH', 
                'message': 'Excessive vibration detected', 
                'parameter': 'vibration', 
                'value': system_data['vibration'] 
            }) 
 
        # Check temperature thresholds 
        if 'temperature' in system_data and system_data['temperature'] 
            alerts.append({ 
                'level': 'CRITICAL', 
                'message': 'Overheating detected', 
                'parameter': 'temperature', 
                'value': system_data['temperature'] 
            }) 
 
        # Log security events 
        if alerts: 
            for alert in alerts: 
                self.security_events.append({ 
                    'timestamp': datetime.now().isoformat(), 
                    'alert': alert 
                }) 
 
        return alerts 
 
    def data_integrity_check(self, data, signature): 
        # Simple data integrity verification 
        data_str = str(data) 
        expected_signature = hashlib.sha256(data_str.encode()).hexdigest() 
        return expected_signature == signature 
 
    def get_security_report(self): 
        critical_count = sum(1 for event in self.security_events 
                             if event['alert']['level'] == 'CRITICAL') 
        high_count = sum(1 for event in self.security_events 
                         if event['alert']['level'] == 'HIGH') 
 
        return { 
            'total_events': len(self.security_events), 
            'critical_alerts': critical_count, 
            'high_alerts': high_count, 
            'last_updated': datetime.now().isoformat() 
        } 
