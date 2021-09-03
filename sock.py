import socket
host=input('introduce el host para el envio : ')
port=int(input('introduce el puerto : '))
usuario=socket.socket()
usuario.connect((host,port))
while True:
	envio=input('Escribe el mensaje perro : ')
	usuario.send(envio.encode())
usuario.close()
