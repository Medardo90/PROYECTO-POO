# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 09:51:07 2022

@author: lab
"""

import tkinter as tk
from tkinter import ttk
from random import randint

raiz= tk.Tk()
raiz.geometry("500×200")

frame1=tk.Frame(raiz)
frame1.place(×=0, y=0, width=250 ,height=200)

label1 = tk.Label(frame1, text="placa")
label1.grid(column=1, row=1, sticky=tk.W, padx=5,dady=5)
entry1=tk.Entry(frame1)
entry1.grid(column=2, row=1, sticky=tk.W, padx=5,dady=5)

label2 = tk.Label(frame1, text="marca")
label2.grid(column=1, row=2, sticky=tk.W, padx=5,dady=5)
entry2=tk.Entry(frame1)
entry2.grid(column=2, row=2, sticky=tk.W, padx=5,dady=5)

colorlista= ["rojo","verde","negro", "azul"]
label3= tk.Label(frame1, text="color")
label3.grid(column=1, row=3, sticky=tk.W, padx=5,dady=5)

combo1= ttk.Combobox(frame1)
entry1=tk.Entry(frame1,values=colorlista)
combo1=set("color")
combo1.grid(column=2, row=2, sticky=tk.W, padx=5,dady=5)

frame2=tk.Frame(raiz)
frame2.place(×=250, y=0, width=250, height=200)

label4 = tk.Label(frame2, text="numero parqueadero")
label4.grid(column=1, row=1, sticky=tk.W, padx=5,dady=5)

raiz.mainloop()