import requests 
print("=== TESTING ORBITAL_STATUS ENDPOINT ===") 
try: 
    r = requests.get('http://localhost:9090/api/orbital_status') 
    print('Status Code:', r.status_code) 
    print('Content Type:', r.headers.get('content-type', 'Not specified')) 
    print('=== RAW RESPONSE ===') 
    print(r.text) 
    print('=== END RESPONSE ===') 
except Exception as e: 
    print('Request Error:', e) 
