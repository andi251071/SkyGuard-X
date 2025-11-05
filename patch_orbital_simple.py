# Simple orbital patch 
import os 
 
# Read app.py 
with open('app.py', 'r') as f: 
    content = f.read() 
 
# Check if orbital code already exists 
if 'orbital_status' in content: 
    print('? Orbital integration already exists in app.py') 
else: 
    print('? Orbital integration NOT found in app.py') 
    print('Please add the integration code manually') 
