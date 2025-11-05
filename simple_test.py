from flask import Flask, jsonify 
app = Flask(__name__) 
 
print("=== LOADING ORBITAL MODULE ===") 
try: 
    from orbital_module.soi_core import SkyportOrbitalInterface 
    soi = SkyportOrbitalInterface() 
    print("? SUCCESS: Orbital module loaded") 
    nodes = soi.simulate_orbital_nodes() 
    print("? Nodes:", nodes) 
    ORBITAL_AVAILABLE = True 
except Exception as e: 
    print("? ERROR:", e) 
    import traceback 
    traceback.print_exc() 
    ORBITAL_AVAILABLE = False 
 
@app.route('/test_simple') 
def test_simple(): 
    if ORBITAL_AVAILABLE: 
        return jsonify({"status": "success", "message": "Orbital working!"}) 
    else: 
        return jsonify({"status": "error", "message": "Orbital failed"}) 
 
if __name__ == '__main__': 
    app.run(debug=True, port=9091) 
