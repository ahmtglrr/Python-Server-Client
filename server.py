#server.py

import socket
import time

#create a socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname()

port=9999

#bind to the port

serversocket.bind((host,port))

serversocket.listen(5)

while True:
    #establish a connection
    clientsocket,addr=serversocket.accept()
    print("Baglanti suradan %s"%str(addr))
    currentTime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()