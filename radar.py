print("Aircraft Radar System") 
print("=" * 40) 
print("This module requires:") 
print(" Internet connection") 
print(" Requests library (pip install requests)") 
print() 
input("Press Enter to scan for aircraft...") 
print("Scanning...") 
try: 
    import requests 
    response = requests.get('https://opensky-network.org/api/states/all', timeout=10) 
    if response.status_code == 200: 
        data = response.json() 
        print(f"? Found {len(data['states'])} aircraft in database") 
        print("Sample aircraft:") 
        for i in range(min(5, len(data['states']))): 
            ac = data['states'][i] 
            callsign = ac[1] if ac[1] else 'UNKNOWN' 
            print(f"  {i+1}. {callsign}") 
    else: 
        print("? Could not fetch aircraft data") 
except ImportError: 
    print("? Requests not installed. Run: pip install requests") 
except Exception as e: 
    print(f"? Error: {e}") 
input("Press Enter to return to menu...") 
