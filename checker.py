import time
import sys
import requests
respuesta=requests.session()
sistema=sys.platform

x=time.gmtime()
x=list(x)
y={x[1]:"ano",x[2]:"mes",x[3]:"dia"}

print(y,'==> esta es la fecha')
time.sleep(1)
#for i in y:
#	print(x,'--> esta es la fecha')
#	print(i)
#	time.sleep(1)
if sistema == "linux":
#	import logo1
	ingresa_url=input("Ingresa la url ==> : ")
	req=respuesta.get(ingresa_url)
#	req=list(req)
	print(req,' ==> Esta es la respuesta de la pagina')
	time.sleep(1)
	print(req.encoding,' ==> Este es el formato de iso del sitio')
	#if req == "<Response [200]>":
	print('A-->SALIR, B--> PEDIR HEADERS, C--> PARA EL CONTENIDO')

	opcion1=input("Ingresa la opcion a realizar |A|,|B|,|C| ")
	#print('A-->SALIR, B--> PEDIR HEADERS, C--> PARA EL CONTENIDO')
	if opcion1=="A":
		print("Terminamos luego este script")
		print("Esto es hecho por alex stone")
	elif opcion1=='B':
		print(req.headers,' ===> Esta es la cabezera')
	elif opcion1=='C':
		print(req.content)
		print('xela-stone')
