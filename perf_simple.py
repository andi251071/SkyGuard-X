import requests  
import time  
print("TEST PERFORMANCE")  
print("================")  
start = time.time()  
try:  
    r = requests.get("https://opensky-network.org/api/states/all", timeout=10)  
    if r.status_code == 200:  
        data = r.json()  
        waktu = time.time() - start  
        print("Waktu: " + str(round(waktu, 2)) + " detik")  
        print("Pesawat: " + str(len(data['states'])))  
    else:  
        print("Gagal: Code " + str(r.status_code))  
except:  
    print("Error koneksi")  
input("Selesai...") 
