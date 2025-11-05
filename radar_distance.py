import requests 
import math 
from datetime import datetime 
 
def calculate_distance(lat1, lon1, lat2, lon2): 
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
 
def get_aircraft_with_distance(): 
    print("???  REAL AIRCRAFT RADAR WITH DISTANCE") 
    print("?? Your Location: Jakarta, Indonesia") 
    print("?? Radar Range: 500 km") 
    print("=" * 60) 
    JAKARTA_LAT = -6.2088 
    JAKARTA_LON = 106.8456 
    try: 
        response = requests.get('https://opensky-network.org/api/states/all', timeout=10) 
        if response.status_code == 200: 
            data = response.json() 
            aircraft_in_range = [] 
            for aircraft in data.get('states', []): 
                if aircraft[5] and aircraft[6]: 
                    ac_lon = aircraft[5] 
                    ac_lat = aircraft[6] 
                    altitude = aircraft[7] or 0 
                    distance = calculate_distance(JAKARTA_LAT, JAKARTA_LON, ac_lat, ac_lon) 
                        aircraft_in_range.append({ 
                            'callsign': aircraft[1] or 'UNKNOWN', 
                            'country': aircraft[2], 
                            'distance_km': round(distance, 1), 
                            'altitude': altitude, 
                            'velocity': aircraft[9] or 0 
                        }) 
            aircraft_in_range.sort(key=lambda x: x['distance_km']) 
            print(f"? Found {len(aircraft_in_range)} aircraft within 500 km") 
            print() 
            print("??  NEARBY AIRCRAFT:") 
            print("-" * 60) 
            for i, ac in enumerate(aircraft_in_range[:8]): 
                print(f"{i+1:2}. {ac['callsign']:12} | {ac['country']:15} | {ac['distance_km']:5} km | Alt: {ac['altitude']:6} ft") 
            print() 
            if aircraft_in_range: 
                print(f"?? Closest aircraft: {aircraft_in_range[0]['distance_km']} km away") 
            print(f"?? Last Update: {datetime.now().strftime('%H:%M:%S')}") 
        else: 
            print("? Could not fetch aircraft data") 
    except Exception as e: 
        print(f"? Error: {e}") 
 
if __name__ == "__main__": 
    get_aircraft_with_distance() 
    print() 
    input("Press Enter to return to menu...") 
