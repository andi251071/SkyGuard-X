# MONETIZATION API SERVER 
from http.server import HTTPServer, BaseHTTPRequestHandler 
import json 
import urllib.parse 
from business_and_governance.data_monetization import DataMonetization 
 
monetization = DataMonetization() 
 
class RevenueAPIHandler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        parsed_path = urllib.parse.urlparse(self.path) 
        query_params = urllib.parse.parse_qs(parsed_path.query) 
 
        # API Key validation 
        api_key = query_params.get('api_key', [None])[0] 
 
        if parsed_path.path == '/api/telemetry': 
            response = monetization.get_drone_telemetry_data(api_key) 
        elif parsed_path.path == '/api/radar': 
            response = monetization.get_radar_analytics(api_key) 
        elif parsed_path.path == '/api/billing': 
            response = monetization.get_billing_report() 
        elif parsed_path.path == '/api/generate_key': 
            customer = query_params.get('customer', ['Demo Customer'])[0] 
            plan = query_params.get('plan', ['basic'])[0] 
            api_key = monetization.generate_api_key(customer, plan) 
            response = {'api_key': api_key, 'customer': customer, 'plan': plan} 
        else: 
            response = {'error': 'Endpoint not found'} 
 
        self.send_response(200) 
        self.send_header('Content-type', 'application/json') 
        self.end_headers() 
        self.wfile.write(json.dumps(response).encode()) 
 
def run_revenue_api(port=8080): 
    server = HTTPServer(('localhost', port), RevenueAPIHandler) 
    print(f"Revenue API Server running on http://localhost:{port}") 
    print("Available endpoints:") 
    print("  GET /api/telemetry?api_key=YOUR_KEY") 
    print("  GET /api/radar?api_key=YOUR_KEY") 
    print("  GET /api/billing") 
    print("  GET /api/generate_key?customer=NAME&plan=basic") 
    server.serve_forever() 
 
if __name__ == '__main__': 
    run_revenue_api() 
