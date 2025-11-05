import http.server
import socketserver
import webbrowser

PORT = 8000

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print("🚀 SkyGuard-X Server running on port", PORT)
    print("📊 Open: http://localhost:8000/command_interface/react_dashboard/enterprise_dashboard.html")
    webbrowser.open("http://localhost:8000/command_interface/react_dashboard/enterprise_dashboard.html")
    httpd.serve_forever()