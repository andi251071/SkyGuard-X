import random 
import time 
from datetime import datetime 
print("Drone Detection System") 
print("=" * 40) 
print("Simulating RF signal detection...") 
print("Monitoring: 2.4GHz, 5.8GHz, 900MHz") 
print() 
input("Press Enter to start drone scan...") 
scan_count = 0 
detections = 0 
try: 
        scan_count += 1 
        print(f"Scan {scan_count}/5...") 
            detections += 1 
            drone_type = random.choice(['DJI Mavic', 'DJI Phantom', 'Custom UAV']) 
            freq = random.choice(['2.4GHz', '5.8GHz']) 
            print(f"?? Detected: {drone_type} on {freq}") 
        else: 
            print("? No drones detected") 
        time.sleep(2) 
    print(f"Scan complete: {detections} drones detected") 
    print("Scan cancelled") 
input("Press Enter to return to menu...") 
