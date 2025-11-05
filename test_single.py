import requests 
print("=== TESTING ENDPOINTS ONE BY ONE ===") 
ECHO is on.
# Test 1 
print("1. Testing /") 
try: 
    r = requests.get('http://localhost:9090/') 
    print(f"   Status: {r.status_code}") 
    print(f"   Response: {r.text}") 
except Exception as e: 
    print(f"   ERROR: {e}") 
ECHO is on.
# Test 2 
print("\\n2. Testing /health") 
try: 
    r = requests.get('http://localhost:9090/health') 
    print(f"   Status: {r.status_code}") 
    print(f"   Response: {r.text}") 
except Exception as e: 
    print(f"   ERROR: {e}") 
ECHO is on.
# Test 3 
print("\\n3. Testing /api/orbital_status") 
try: 
    r = requests.get('http://localhost:9090/api/orbital_status') 
    print(f"   Status: {r.status_code}") 
    print(f"   Response: {r.text}") 
except Exception as e: 
    print(f"   ERROR: {e}") 
ECHO is on.
# Test 4 
print("\\n4. Testing /api/system_status_enhanced") 
try: 
    r = requests.get('http://localhost:9090/api/system_status_enhanced') 
    print(f"   Status: {r.status_code}") 
    print(f"   Response: {r.text}") 
except Exception as e: 
    print(f"   ERROR: {e}") 
