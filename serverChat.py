#Programa Servidor para realizar una conexión via Socket al localhost
#Llamar la ubicación de python

#!/usr/bin/env python
 
import socket

serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creación de Socket en la variable serverSocket

serversocket.bind(('localhost', 8000)) #Ip y puerto para establecer la conexión, usamos
#esta función para mantener en escucha el puerto, en este caso la ip estática de la PC servidor.

print "Esperando Conexión"

serversocket.listen(True) #El servidor se pone en escucha.

clientsocket, clientaddress = serversocket.accept() #Socket del cliente, Direccion Ip del cliente y se acepta conexión.


print 'La conexión se establecio con: ', clientaddress #Se muestra Ip del cliente

while True:
        data = clientsocket.recv(1024) #Se recibe mensaje
        print data  #Se imprime el mensaje del cliente.
        newdata = 'Mensaje Recibido, Finalizo la conexión' #Mensaje que contesta el cliente
        clientsocket.send(newdata) #Envio del mensaje y termina conexion con ese cliente.
        serversocket.listen(True) #El servidor se mantiene en escucha por si otro cliente requiere conectarse.
        clientsocket, clientaddress = serversocket.accept() #Se acepta una nueva petición.

clientsocket.close() #Se cierra la comunicación.
