import jwt  
from datetime import datetime, timedelta  
from functools import wraps  
from flask import request, jsonify  
  
class ZeroTrustAuth:  
    def __init__(self):  
        self.secret_key = "super-secure-key-2024"  
  
    def generate_token(self, user_id, roles):  
        payload = {  
            "user_id": user_id,  
            "roles": roles,  
            "exp": datetime.utcnow() + timedelta(hours=4)  
        }  
        return jwt.encode(payload, self.secret_key, algorithm="HS256")  
  
    def verify_token(self, token):  
        try:  
            if token.startswith("Bearer "):  
                token = token[7:]  
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])  
            return payload  
        except:  
            return None  
  
def require_auth(f):  
    @wraps(f)  
    def decorated(*args, **kwargs):  
        token = request.headers.get("Authorization", "")  
        auth = ZeroTrustAuth()  
        payload = auth.verify_token(token)  
        if not payload:  
            return jsonify({"error": "Unauthorized"}), 401  
        return f(*args, **kwargs)  
