import sys
import os
print("""

	$-Seleciona [h] para informacion del hash
	$-Selecciona [v] para la version

	$-Seleccione [c] para Crear archivos
	$-Si quieres hacar uso del sistema [a]
""")

a=input("proprciona la operacion a realizar ==>: ")
if a == "h":
	x=sys.hash_info
	xx=sys.modules
	print("Esta es la informaciondel hash ==> : ",x," los modulos ==> ",xx)
	#for i in xx:
	#	print(i)
elif a == "v":
	y=sys.version
	yy=sys.platform
	print("esta es la versionde system --> : ",y, "la plataforna usada es --> ",yy)

elif a == "c":
	ruta=input("Introduce la ruta ==> : ")
	if (ruta==" "): os.getcwd()+"\\"
	if(os.path.isdir(ruta)):
		nombre=input("nombre del achivo ==> : ")
		manejo=open(ruta+nombre,"w")
		manejo.close()
		print("Esta carpeta a esta creada ",nombre)
elif a =="a":
	s=os.system("ifconfig")
	t=os.sysconf_names
	print(s)
	for i in t:
		print(i)
#else:
#	print("reinicie e programa")

