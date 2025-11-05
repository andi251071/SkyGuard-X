@echo off  
python -c "import socket, webbrowser; s=socket.socket(); s.bind(('0.0.0.0',9090)); s.listen(5); print('Starting...'); webbrowser.open('http://localhost:9090'); print('Server ready'); import time; time.sleep(999)"  
