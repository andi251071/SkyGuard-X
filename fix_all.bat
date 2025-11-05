@echo off 
echo ==================================================== 
echo         COMPLETE DASHBOARD FIX                    
echo ==================================================== 
echo. 
echo Step 1: Recreating web_server.py... 
del command_interface\web_server.py 2>nul 
 
echo from http.server import HTTPServer, SimpleHTTPRequestHandler 
echo import webbrowser 
echo. 
echo def start_web_server(): 
echo     server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler) 
echo     print("SkyGuard-X Web Server Started") 
echo     print("Access at: http://localhost:8000") 
echo     print("Dashboard: http://localhost:8000/command_interface/react_dashboard/enterprise_dashboard.html") 
echo     server.serve_forever() 
echo. 
echo if __name__ == "__main__": 
echo     start_web_server() 
 
echo Step 2: Verifying dashboard files... 
if not exist "command_interface\react_dashboard\enterprise_dashboard.html" ( 
    echo Creating basic dashboard... 
    echo <h1>SkyGuard-X Dashboard</h1> 
    echo <p>Enterprise Dashboard is Working</p> 
) 
 
echo Step 3: Starting web server... 
python command_interface\web_server.py 
 
pause 
