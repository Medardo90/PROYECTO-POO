from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox, ttk
from PIL import ImageTk, Image

root = Tk()
root.geometry("550x600")
root.title("Proyecto(BANDA TRANSPORTADORA DE CAJAS)")


titulo=Label(root,text="Banda de Transportadores")
titulo.place(x=50, y=20)
titulo1=Label(root,text="Distribucion de materiales")
titulo1.place(x=50, y=40)


image= Image.open("cinta.png") 
image= image.resize((350,330), Image.ANTIALIAS) 
image=ing= ImageTk.PhotoImage(image)
lb1_ing=Label(image=ing)
Label(image=ing).place(x=190, y=60)


imag= Image.open("motor2.png") 
imag= imag.resize((60,60), Image.ANTIALIAS) 
imag=ing2= ImageTk.PhotoImage(imag)
lb2_ing=Button(imag=ing2)
Button(imag=ing2).place(x=350, y=15)
ima= Image.open("motor2.png") 
ima= ima.resize((60,60), Image.ANTIALIAS) 
ima=ing2= ImageTk.PhotoImage(ima)
lb3_ing=Button(ima=ing2)
Button(ima=ing2).place(x=350, y=325)


button1=Button(root,text="Encendido")
button1.place(x=420, y=20)
button2=Button(root,text="  Apagado ")
button2.place(x=420, y=50)
button3=Button(root,text="Encendido")
button3.place(x=420, y=330)
button4=Button(root,text="  Apagado ")
button4.place(x=420, y=360)


titulo3=Button(root,text="       MODO MANUAL CARRO   ")
titulo3.place(x=15, y=400)
frame2 = Frame(root, padx=0.3, pady=0.4)
frame2.place(x=15,y=430)
Button(frame2, text='        Adelante         ', padx=1).grid(row=22,column=0)
Button(frame2, text='    Atras    ', padx=1).grid(row=22,column=1)
Button(frame2, text='Parar', padx=13).grid(row=23,column=1)
accion = Label(frame2,text = "Accion").grid(row=23,column=0)
space = Label(frame2,text = "--------------------").grid(row=24,column=0)
space = Label(frame2,text = "------------").grid(row=24,column=1)
space = Label(frame2,text = "    ").grid(row=24,column=2)
velocidad1 = Label(frame2,text = "Velocidad de Carro").grid(row=25,column=0)
Entry(frame2, width = 8).grid(row=25,column=1)
porcent = Label(frame2, text='%', padx=1).grid(row=25,column=2)
velocidad2 = Label(frame2,text = "Velocidad de Rotor").grid(row=26,column=0)
Entry(frame2, width = 8).grid(row=26,column=1)
porcent = Label(frame2, text='%', padx=1).grid(row=26,column=2)


titulo4=Button(root,text="            MODO AUTO CARRO        ")
titulo4.place(x=225, y=400)
frame3 = Frame(root, padx=0.3, pady=0.4)
frame3.place(x=225,y=430)
Posicion = Label(frame3,text = "Posicion del Carro").grid(row=22,column=4)
Entry(frame3, width = 8).grid(row=22,column=5)
porcent = Label(frame3, text='%', padx=1).grid(row=22,column=6)
Posicion = Label(frame3,text = "TAR: Tiempo Pausa").grid(row=23,column=4)
Entry(frame3, width = 8).grid(row=23,column=5)
porcent = Label(frame3, text='%', padx=1).grid(row=23,column=6)
Posicion = Label(frame3,text = "ACT: Tiempo Pausa").grid(row=24,column=4)
Entry(frame3, width = 8).grid(row=24,column=5)
porcent = Label(frame3, text='%', padx=1).grid(row=24,column=6)
space = Label(frame3,text = "--------------------").grid(row=25,column=4)
space = Label(frame3,text = "--------------").grid(row=25,column=5)
Button(frame3, text='        Habilitar         ', padx=1).grid(row=26,column=4)
Button(frame3, text='    Deshabilitar    ', padx=1).grid(row=26,column=5)


frame4 = Frame(root, padx=0.3, pady=0.4)
frame4.place(x=15,y=90)
Parada_s = Label(frame4,text = "Paradas por sobrecarga").grid(row=22,column=0)
Entry(frame4, width = 8).grid(row=22,column=1)
space = Label(frame4,text = " ").grid(row=22,column=2)
Button(frame4, text='Reset', padx=1).grid(row=22,column=3)
Posicion = Label(frame4,text = "TAR: Tiempo Pausa").grid(row=23,column=0)
Entry(frame4, width = 8).grid(row=23,column=1)
space = Label(frame4,text = " ").grid(row=23,column=2)
Button(frame4, text='Reset', padx=1).grid(row=23,column=3)
Posicion = Label(frame4,text = "ACT: Tiempo Pausa").grid(row=24,column=0)
Entry(frame4, width = 8).grid(row=24,column=1)
space = Label(frame4,text = " ").grid(row=24,column=2)
Button(frame4, text='Reset', padx=1).grid(row=24,column=3)

titulo1=Label(root,text="Aire Limpieza")
titulo1.place(x=90, y=190)
ON=Button(root,text="ON")
ON.place(x=15, y=210)
OFF=Button(root,text="OFF")
OFF.place(x=50, y=210)

ima= Image.open("reinicio.png") 
ima= ima.resize((30,20), Image.ANTIALIAS) 
ima=ing= ImageTk.PhotoImage(ima)
lb1_ing=Button(ima=ing)
Button(ima=ing).place(x=90, y=210)

im= Image.open("g.png") 
im= im.resize((180,135), Image.ANTIALIAS) 
im=ing= ImageTk.PhotoImage(im)
lb1_ing=Button(im=ing)
Label(im=ing).place(x=15, y=245)


root.mainloop()