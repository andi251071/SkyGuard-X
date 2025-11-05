from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): 
    return "DRONE SYSTEM READY ?" 
@app.route("/health") 
def health(): 
    return "Status: ACTIVE" 
# ======== SKYPORT ORBITAL INTERFACE INTEGRATION ========
try:
    from orbital_module.soi_core import SkyportOrbitalInterface
    ORBITAL_MODULE_AVAILABLE = True
    soi = SkyportOrbitalInterface()
    print("✅ Skyport Orbital Interface loaded successfully")
except ImportError as e:
    ORBITAL_MODULE_AVAILABLE = False
    print(f"⚠️ Orbital module not available: {e}")

@app.route('/api/orbital_status')
def orbital_status():
    if not ORBITAL_MODULE_AVAILABLE:
        return jsonify({"status": "module_not_available", "message": "Orbital module not installed"})
    
    return jsonify({
        "status": "operational",
        "orbital_nodes": soi.simulate_orbital_nodes(),
        "quantum_encryption": "active",
        "ground_station": "SKYPORT-JKT-01",
        "message": "Skyport Orbital Interface is running"
    })

@app.route('/api/system_status_enhanced')
def system_status_enhanced():
    status = {
        "radar_system": "operational",
        "ai_server": "operational", 
        "alert_system": "operational",
        "orbital_module": "available" if ORBITAL_MODULE_AVAILABLE else "unavailable",
        "quantum_encryption": "active" if ORBITAL_MODULE_AVAILABLE else "inactive"
    }
    return jsonify(status)
# ======== END ORBITAL INTEGRATION ========
# ======== SKYPORT ORBITAL INTERFACE INTEGRATION ========
from flask import jsonify  # <-- TAMBAH BARIS INI
try:
    from orbital_module.soi_core import SkyportOrbitalInterface
    ORBITAL_MODULE_AVAILABLE = True
    soi = SkyportOrbitalInterface()
    print("✅ Skyport Orbital Interface loaded successfully")
except ImportError as e:
    ORBITAL_MODULE_AVAILABLE = False
    print(f"⚠️ Orbital module not available: {e}")
# ... rest of the code ...
if __name__ == "__main__": 
    print("Server starting...") 
    app.run(host="0.0.0.0", port=9090, debug=True) 
