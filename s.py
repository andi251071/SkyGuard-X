import socket  
import webbrowser  
s = socket.socket()  
s.bind(("0.0.0.0", 9090))  
s.listen(5)  
print("Server ready - http://localhost:9090")  
webbrowser.open("http://localhost:9090")  
while True:  
"    client, addr = s.accept()"  
"    client.send(b'HTTP/1.1 200 OK\\r\\nContent-Type: text/html\\r\\n\\r\\n<h1>Drone System Active</h1>')"  
"    client.close()"  
"    print('Client connected')"  
