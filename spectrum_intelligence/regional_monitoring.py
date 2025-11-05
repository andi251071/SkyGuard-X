import requests 
import math 
print("=== RADAR JAKARTA ===") 
print("Cari pesawat dekat Jakarta...") 
jarak_total = 0 
jumlah = 0 
try: 
    r = requests.get('https://opensky-network.org/api/states/all', timeout=10) 
    if r.status_code == 200: 
        data = r.json() 
        for i in range(min(20, len(data['states']))): 
            p = data['states'][i] 
            if p[1]: 
                print(f"{i+1}. {p[1]:10} - {p[2]:20}") 
        print(f"Total: {len(data['states'])} pesawat terdeteksi") 
    else: 
        print("Gagal ambil data") 
except Exception as e: 
    print(f"Error: {e}") 
input("Tekan Enter...") 
