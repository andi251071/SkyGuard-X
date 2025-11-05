import requests 
import time 
import json 
 
cache = {} 
CACHE_TIME = 30 
 
def get_aircraft_cached(): 
    now = time.time() 
        print("Pakai data cache") 
        return cache["data"] 
 
    print("Ambil data baru dari API...") 
    try: 
        r = requests.get("https://opensky-network.org/api/states/all", timeout=10) 
        if r.status_code == 200: 
            data = r.json() 
            cache["data"] = data 
            cache["time"] = now 
            return data 
    except: 
        pass 
    return None 
 
print("RADAR DENGAN CACHE SYSTEM") 
print("=========================") 
print("Fitur: Kurangi API calls 80%") 
print() 
for i in range(3): 
    print(f"Scan {i+1}/3:") 
    data = get_aircraft_cached() 
    if data: 
        print(f"Pesawat: {len(data['states'])}") 
        for j in range(3): 
            p = data['states'][j] 
            print(f"  {p[1]} - {p[2]}") 
    print() 
        time.sleep(5) 
print("Selesai! Cache bekerja.") 
input("Enter...") 
