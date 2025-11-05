import requests  
import time  
print("PERFORMANCE CHECKER")  
print("===================")  
start_time = time.time()  
try:  
    r = requests.get("https://opensky-network.org/api/states/all", timeout=10)  
    if r.status_code == 200:  
        data = r.json()  
        end_time = time.time()  
        response_time = end_time - start_time  
        print(f"? RESPONSE TIME: {response_time:.2f} detik")  
        print(f"? PESAWAT: {len(data['states'])}")  
        print(f"? DATA SIZE: {len(str(data)) // 1024} KB")  
