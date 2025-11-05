import requests 
import math 
print("MENCARI PESAWAT TERDEKAT...") 
try: 
    r = requests.get('https://opensky-network.org/api/states/all', timeout=10) 
    if r.status_code == 200: 
        data = r.json() 
        print(f"SUKSES: {len(data['states'])} pesawat terdeteksi") 
        for i in range(5): 
            p = data['states'][i] 
            print(f"{i+1}. {p[1]} - {p[2]}") 
    else: 
        print("GAGAL: Tidak bisa ambil data") 
except: 
    print("ERROR: Cek internet") 
input("Selesai...") 
