@echo off 
echo ?? Creating app_enhanced.py... 
 
echo from flask import Flask, jsonify, send_file 
echo import sqlite3 
echo import joblib 
echo from datetime import datetime 
echo. 
echo app = Flask(__name__) 
echo. 
echo try: 
echo     model = joblib.load("predictive_maintenance_model.pkl") 
echo     ai_loaded = True 
echo     print("AI Model loaded!") 
echo except: 
echo     ai_loaded = False 
echo. 
echo @app.route("/") 
echo def dashboard(): 
echo     return send_file("dashboard_enhanced.html") 
echo. 
echo @app.route("/api/health") 
echo def health(): 
echo     return jsonify({"status": "ok"}) 
echo. 
echo if __name__ == "__main__": 
echo     print("Server starting...") 
echo     app.run(port=5000) 
 
echo ? app_enhanced.py created! 
pause 
