@echo off  
cd /d C:\DroneDefense  
python -c "import socket,webbrowser; s=socket.socket(); s.bind(('0.0.0.0',9090)); s.listen(5); print('Drone System Started'); webbrowser.open('http://localhost:9090'); exec('while True: c,a=s.accept(); c.send(b''HTTP/1.1 200 OK\\r\\n\\r\\n^<h1^>Drone System Running^</h1^>''); c.close()')" 
