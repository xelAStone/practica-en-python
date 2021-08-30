import os
import time
x="""
>>>>>>>>> a para listar los archivos
>>>>>>>>> b para buscar el interprete de python 
>>>>>>>>> c para activar wireshark
>>>>>>>>> d

....	....	....	....
\          /	|   \  /   |
 \        /	|    \/    |
  \      /	|	   |
   \    /	|	   |
    \  /	|   /00\   |
     \/		|__/	\__|

.............................
"""
ti=time.gmtime()
ti=list(ti)
print(x,ti[:1]," nueva version")
opcion=input("SELECCIONA [a] [b]  [c]  [d] ===> : ")
lalo="""
	alex	stone
alex	stone
"""
for i in lalo:
	print(i)
	time.sleep(.2)
if opcion=="a":
	os.system("ls -la")
	print("los archivos")
elif opcion=="b":
	os.system("apt search python3")
	print("lalo")
elif opcion=="c":
	os.system("wireshark")
	print("instalacion completa")

else:
	print("programa finalizado")
	print(time.time())
