import socket
port=int(input('introduce el puerto de escucha '))
servicio=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
servicio.bind((socket.gethostname(),port))
servicio.listen(4)
x,y=servicio.accept()
while True:
	variable=x.recv(1024)
	x.send(variable)
	print(y[0],y[1],'--> este es la direccion del usuario')
x.close()
