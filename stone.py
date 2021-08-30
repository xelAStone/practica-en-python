from tkinter import *
#----raiz de la ventana------
raiz=Tk()
raiz.geometry('450x500')
raiz.title('===CALCULADORA===')
frame=Frame(raiz)
frame.pack()
#-----menu de cascada-----
menu=Menu(raiz)
raiz.config(menu=menu,width=250,height=200)
menu2=Menu(menu, tearoff=0)
menu2.add_command(label='salir',command=raiz.destroy)
menu.add_cascade(label='Opcion',menu=menu2)




#--------funciones------
variable=''
texto=StringVar()
variable2=0
#funcion para visualizar en pantalla
def funcion(numero):
	global variable
	if variable!='':
		texto.set(numero)
		variable=''
	else:
		texto.set(texto.get()+numero)
#funcion para calculo 
def funcion2(nume):
	global variable
	global variable2
	variable2=+int(nume)
	variable='+'
	texto.set(variable2)
#funcion para muestra de resultados
def funcion3():
	global variable
	texto.set(variable2+int(texto.get()))
#funcion para limpiar en pantalla
def funcion4():
	global variable
	variable=('')
	texto.set('')
ventana=Entry(frame,textvariable=texto)
ventana.pack()
frame2=Frame(raiz)
frame2.pack()
#--------funciones ------------



#--------botones-----------
boton1=Button(frame2,text='1',command=lambda:funcion('1'))
boton1.grid(row=1,column=0,padx=12,pady=12)
boton1.config(bg='green2',relief='groove',bd=8)
boton2=Button(frame2,text='2',command=lambda:funcion('2'))
boton2.grid(row=1,column=1,padx=12,pady=12)
boton2.config(bg='green2',relief='groove',bd=8)
boton3=Button(frame2,text='3',command=lambda:funcion('3'))
boton3.grid(row=1,column=2,padx=12,pady=12)
boton3.config(bg='green2',relief='groove',bd=8)
boton4=Button(frame2,text='4',command=lambda:funcion('4'))
boton4.grid(row=2,column=0,padx=12,pady=12)
boton4.config(bg='green2')
boton5=Button(frame2,text='5',command=lambda:funcion('5'))
boton5.grid(row=2,column=1,padx=12,pady=12)
boton5.config(bg='green2')
boton6=Button(frame2,text='6',command=lambda:funcion('6'))
boton6.grid(row=2,column=2,padx=12,pady=12)
boton6.config(bg='green2')
boton7=Button(frame2,text='7',command=lambda:funcion('7'))
boton7.grid(row=3,column=0,padx=12,pady=12)
boton7.config(bg='green2')
boton8=Button(frame2,text='8',command=lambda:funcion('8'))
boton8.grid(row=3,column=1,padx=12,pady=12)
boton8.config(bg='green2')
boton9=Button(frame2,text='9',command=lambda:funcion('9'))
boton9.grid(row=3,column=2,padx=12,pady=12)
boton9.config(bg='green2')
boton_cero=Button(frame2,text='0',command=lambda:funcion('0'))
boton_cero.grid(row=4,column=0,padx=12,pady=12)
boton_cero.config(bg='green2')
boton_suma=Button(frame2,text='+',command=lambda:funcion2(texto.get()))
boton_suma.grid(row=4,column=1,padx=12,pady=12)
boton_suma.config(bg='green2')
boton_resta=Button(frame2,text='-')
boton_resta.grid(row=4,column=2,padx=12,pady=12)
boton_resta.config(bg='green2')
boton_limpiar=Button(frame2,text='C',command=lambda:funcion4())
boton_limpiar.grid(row=5,column=1,padx=12,pady=12)
boton_resultado=Button(frame2,text='=',command=lambda:funcion3())
boton_resultado.grid(row=6,column=1,padx=12,pady=12)




raiz.mainloop()
