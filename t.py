import requests 
r=requests.get('http://localhost:9090/api/orbital_status') 
print(r.status_code)   
print(r.text) 
