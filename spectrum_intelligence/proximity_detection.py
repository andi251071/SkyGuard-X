import requests 
import math 
from datetime import datetime 
 
def hitung_jarak(lat1, lon1, lat2, lon2): 
    R = 6371 
    lat1_rad = math.radians(lat1) 
    lon1_rad = math.radians(lon1) 
    lat2_rad = math.radians(lat2) 
    lon2_rad = math.radians(lon2) 
    dlat = lat2_rad - lat1_rad 
    dlon = lon2_rad - lon1_rad 
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a)) 
    return R * c 
 
print("RADAR PESAWAT - JARAK REAL-TIME") 
print("================================") 
print("Lokasi: Jakarta, Indonesia") 
print("Jangkauan: 500 km") 
print("Jangkauan: 500 km") 
print("Lokasi: Jakarta, Indonesia") 
print() 
JAKARTA_LAT = -6.2088 
JAKARTA_LON = 106.8456 
 
try: 
    print("Mengambil data pesawat...") 
    response = requests.get('https://opensky-network.org/api/states/all', timeout=10) 
    if response.status_code == 200: 
        data = response.json() 
        pesawat_dekat = [] 
 
        for pesawat in data.get('states', []): 
            if pesawat[5] and pesawat[6]: 
                lon = pesawat[5] 
                lat = pesawat[6] 
                jarak = hitung_jarak(JAKARTA_LAT, JAKARTA_LON, lat, lon) 
 
                    pesawat_dekat.append({ 
                        'callsign': pesawat[1] or 'UNKNOWN', 
                        'negara': pesawat[2], 
                        'jarak': round(jarak, 1), 
                        'tinggi': pesawat[7] or 0 
                    }) 
 
        pesawat_dekat.sort(key=lambda x: x['jarak']) 
 
        print(f"Ditemukan: {len(pesawat_dekat)} pesawat dalam 500 km") 
        print() 
        if pesawat_dekat: 
            print("10 PESAWAT TERDEKAT:") 
            print("-------------------") 
            for i, p in enumerate(pesawat_dekat[:10]): 
                print(f"{i+1}. {p['callsign']} - {p['negara']} - {p['jarak']} km - {p['tinggi']} kaki") 
 
            print() 
            print(f"PESAWAT TERDEKAT: {pesawat_dekat[0]['jarak']} km") 
        else: 
            print("Tidak ada pesawat dalam jangkauan") 
 
    else: 
        print("Gagal mengambil data") 
 
except Exception as e: 
    print(f"Error: {e}") 
 
input("Tekan Enter...") 
