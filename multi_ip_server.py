import socket  
server = socket.socket()  
server.bind(('0.0.0.0', 9090))  
server.listen(5)  
print("=" * 50)  
print("?? DRONE DEFENSE SYSTEM - MULTI IP ACCESS")  
print("?? Akses dari browser:")  
print("   1. http://localhost:9090")  
print("   2. http://127.0.0.1:9090")  
print("   3. http://10.211.59.67:9090")  
print("   4. http://172.20.208.1:9090")  
print("=" * 50)  
while True:  
    client, addr = server.accept()  
    request = client.recv(1024).decode()  
    html = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'  
    html += '<html><body style=\"font-family: Arial; margin: 40px;\">'  
    html += '<h1>??? Drone Defense System</h1>'  
    html += '<p>Status: <span style=\"color: green;\">ACTIVE ?</span></p>'  
    html += '<h3>IP Address System Anda:</h3>'  
    html += '<ul><li>10.211.59.67</li><li>172.20.208.1</li></ul>'  
    html += '<p>Gunakan IP di atas untuk akses dari device lain</p>'  
    html += '</body></html>'  
    client.send(html.encode())  
    client.close()  
