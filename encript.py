import base64

x=b'NDIxMzE2LDQxNTIzMSw1NDcwNDYsNDgzMDMwLDU0NzQ4NCw0NzcyMTMsNDc3Mjkx'
#print(x)
xx=b'NDI5NjcyLDQyMDAyNyw0MjIxMDEsNDI1Nzg4LDQyMjA2MQ=='
xxx=b'NDI3NTE0LDQyNjY4NSw0MjMwNjcsNDI2MTUwLDQyMTY4MQ=='

ingresa=input("Por favor ingresa |a| para imprimir los bines encriptados \n                  |b| para ver mas bines encriptados ====> : ")
if ingresa=="a":
	print(x)
	op1=input("elige \n |start| para desecriptar el archivo \n |salir| para fializar el prograna ----> : ")
	if op1=="start":
		deco=base64.b64decode(x)
		print(deco,' Este es el achivo ')

	elif op1=="salir":
		print("programa finalizado")
elif ingresa=="b":
	print(xx,' op1')
	print(xxx, 'op2')
	op2=input("ingrese |op1| para el primer archivo o |op2| para el segundo archivo ---> : ")
	if op2=="op1":
		deco=base64.b64decode(xx)
		print(deco, " ==> este es el archivo")
	elif op2=="op2":
		deco=base64.b64decode(xxx)
		print(deco," ==> este es el archivo")
else:
	print("no se encontro la orden, reinicie el programa")

