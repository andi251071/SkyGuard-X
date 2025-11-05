import requests  
import math  
from datetime import datetime  
  
def hitung_jarak(lat1, lon1, lat2, lon2):  
    return 6371 * math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(lon2-lon1)))  
  
JAKARTA_LAT = -6.2088  
JAKARTA_LON = 106.8456  
  
try:  
    print("???  RADAR PESAWAT REAL-TIME")  
    print("?? Lokasi: Jakarta, Indonesia")  
    print("?? Jangkauan: 500 km")  
    print("=" * 50)  
    response = requests.get('https://opensky-network.org/api/states/all', timeout=10)  
    if response.status_code == 200:  
        data = response.json()  
        pesawat_dekat = []  
        for p in data.get('states', []):  
            if p[5] and p[6]:  
                jarak = hitung_jarak(JAKARTA_LAT, JAKARTA_LON, p[6], p[5])  
