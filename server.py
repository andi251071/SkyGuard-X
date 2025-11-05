import socket 
server = socket.socket() 
server.bind(("0.0.0.0", 9090)) 
server.listen(5) 
print("Drone System Ready! Open: http://localhost:9090") 
while True: 
    client, addr = server.accept() 
    request = client.recv(1024) 
    html = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" 
    html += "<html><body><h1>Drone Defense System</h1><p>Status: ACTIVE</p></body></html>" 
    client.send(html.encode()) 
    client.close() 
