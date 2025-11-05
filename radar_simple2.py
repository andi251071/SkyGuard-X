import requests  
import time  
print("RADAR SIMPLE - TEST CACHE")  
print("========================")  
cache = {}  
def get_data():  
    if "data" in cache:  
        print("Pakai cache")  
        return cache["data"]  
    print("Ambil data baru")  
    try:  
        r = requests.get("https://opensky-network.org/api/states/all", timeout=10)  
        if r.status_code == 200:  
            data = r.json()  
            cache["data"] = data  
            return data  
    except:  
        return None  
for i in range(2):  
    print(f"Test {i+1}:")  
    data = get_data()  
    if data:  
        print(f"Pesawat: {len(data['states'])}")  
    time.sleep(2)  
print("Cache system work!")  
input("Enter...") 
