with open('app.py', 'r') as f: 
    content = f.read() 
 
has_orbital = 'orbital_status' in content 
has_module = 'ORBITAL_MODULE_AVAILABLE' in content 
 
if has_orbital: 
    print('Endpoint orbital_status: ? ADA') 
else: 
    print('Endpoint orbital_status: ? TIDAK ADA') 
 
if has_module: 
    print('Integration code: ? ADA') 
else: 
    print('Integration code: ? TIDAK ADA') 
