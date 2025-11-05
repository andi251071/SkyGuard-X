from flask import Flask, jsonify 
app = Flask(__name__) 
 
print("DRONE SYSTEM STARTING...") 
 
try: 
    from orbital_module.soi_core import SkyportOrbitalInterface 
    soi = SkyportOrbitalInterface() 
    ORBITAL_AVAILABLE = True 
    print("ORBITAL MODULE LOADED") 
except: 
    ORBITAL_AVAILABLE = False 
    print("ORBITAL MODULE UNAVAILABLE") 
 
@app.route('/') 
def home(): 
    return "DRONE SYSTEM OK" 
 
@app.route('/api/orbital') 
def orbital(): 
    if ORBITAL_AVAILABLE: 
        return jsonify({'status': 'active', 'nodes': soi.simulate_orbital_nodes()}) 
    else: 
        return jsonify({'status': 'inactive'}) 
 
if __name__ == '__main__': 
    app.run(debug=True, port=9090) 
