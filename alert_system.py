import requests  
import math  
import time  
from datetime import datetime  
  
JAKARTA_LAT = -6.2088  
JAKARTA_LON = 106.8456  
  
def cek_ancaman():  
    try:  
        response = requests.get('https://opensky-network.org/api/states/all', timeout=10)  
        if response.status_code == 200:  
            data = response.json()  
            for p in data.get('states', []):  
                if p[5] and p[6] and p[7]:  
                    jarak = 6371 * math.acos(math.sin(math.radians(JAKARTA_LAT)) * math.sin(math.radians(p[6])) + math.cos(math.radians(JAKARTA_LAT)) * math.cos(math.radians(p[6])) * math.cos(math.radians(p[5]-JAKARTA_LON)))  
