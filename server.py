#server.py

import socket
import time

#soket kurulumu
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


host = socket.gethostname()

port=9999

#Portumuzu dinlemeye alıyoruz

serversocket.bind((host,port))

serversocket.listen(5)

while True:
    clientsocket,addr=serversocket.accept()
    print("Baglanti suradan %s"%str(addr))
    currentTime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
