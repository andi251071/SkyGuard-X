from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): 
    return "DRONE SYSTEM READY ?" 
@app.route("/health") 
def health(): 
    return "Status: ACTIVE" 
if __name__ == "__main__": 
    print("Server starting...") 
    app.run(host="0.0.0.0", port=9090, debug=True) 
