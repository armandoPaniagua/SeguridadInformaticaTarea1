import socket

socki=socket.socket()       
host=socket.getfqdn()   
port=8080
socki.bind((host,port))     

print('Starting server on',host,port)

print('The Web server URL for this would be http://%s:%d/'%(host,port))
socki.listen(5)             
print('Entering infinite loop; hit CTRL-C to exit')
while True:
    #Establish connection with client.
    c,(client_host,client_port)=socki.accept()
    print('Got connection from',client_host,client_port)
    #c.send('Server Online\n')
    c.recv(1000)
    c.send(b'HTTP/1.0 200 OK\n')
    c.send(b'Content-Type: text/html\n')
    c.send(b'\n')
    fileHTML=open("index.html","rb")
    for line in fileHTML.readlines():
        c.send(line)
        
    c.close()
