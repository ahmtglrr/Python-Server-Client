#client.py
import socket

#create a socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host=socket.gethostname()

port=9999

s.connect((host,port))

tm=s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))