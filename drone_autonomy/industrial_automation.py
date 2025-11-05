# INDUSTRIAL AUTOMATION SYSTEM 
from datetime import datetime 
import time 
 
class IndustrialAutomation: 
    def __init__(self): 
        self.automation_rules = [] 
        self.operation_log = [] 
        print("Industrial Automation System Initialized") 
 
    def add_automation_rule(self, rule_name, condition, action): 
        rule = { 
            'name': rule_name, 
            'condition': condition, 
            'action': action, 
            'enabled': True 
        } 
        self.automation_rules.append(rule) 
        return f"Rule '{rule_name}' added" 
 
    def evaluate_rules(self, sensor_data): 
        triggered_actions = [] 
 
        for rule in self.automation_rules: 
            if rule['enabled']: 
                # Simple condition evaluation 
                condition_met = self._evaluate_condition(rule['condition'], sensor_data) 
                if condition_met: 
                    triggered_actions.append({ 
                        'rule': rule['name'], 
                        'action': rule['action'], 
                        'timestamp': datetime.now().isoformat() 
                    }) 
 
        # Log the automation event 
        if triggered_actions: 
            self.operation_log.extend(triggered_actions) 
 
        return triggered_actions 
 
    def _evaluate_condition(self, condition, sensor_data): 
        # Simple condition parser 
        try: 
            param = condition['parameter'] 
            operator = condition['operator'] 
            value = condition['value'] 
 
            if param not in sensor_data: 
                return False 
 
            sensor_value = sensor_data[param] 
 
            if operator == '
                return sensor_value 
            elif operator == '==': 
                return sensor_value == value 
            elif operator == '
                return sensor_value 
 
        except Exception as e: 
            print(f"Condition evaluation error: {e}") 
            return False 
 
        return False 
 
    def get_automation_status(self): 
        enabled_rules = [rule for rule in self.automation_rules if rule['enabled']] 
        return { 
            'total_rules': len(self.automation_rules), 
            'enabled_rules': len(enabled_rules), 
            'recent_actions': len(self.operation_log), 
            'last_updated': datetime.now().isoformat() 
        } 
