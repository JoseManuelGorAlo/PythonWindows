
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from tkinter import *
from pantalla2 import ventanaAlta
from pantallaPrincipal import ventanaBajas
from Informes import ventanaInformes
from nominas import ventanaNominas
from tkinter import ttk
import sqlite3
con=sqlite3.connect("empresa.db")
cur=con.cursor()
cur.execute("create table if not exists empleados(codigo integer not null primary key unique, nombre varchar(50), fechaInicio date, fechaFin date, direccion varchar(50), nif varchar(50), iban varchar(50), numeroSS varchar(50), genero varchar(50), departamento varchar(50), puesto varchar(50), telefono varchar(50), email varchar(50), salariomensual decimal, pagasExtra decimal, IRPF decimal, SSSS decimal)")

root = Toplevel()
root.config(bd=15)
root.resizable(0,0)
root.iconbitmap("descarga.ico")
root.title("Paco&CO")
root.geometry('650x400+300+500')


imgita = PhotoImage(file = 'descarga.png')
label = ttk.Label(root, image=imgita)
PhotoImage(file = 'descarga.png')
label.pack()



b = Button(root, text="ALTAS", width=10,command=ventanaAlta)
b.config(fg="white",bg="black",)
b1 = Button(root, text="BAJAS", width=10, command=ventanaBajas)
b1.config(fg="white",bg="black")
b2 = Button(root, text="INFORMES", width=10, command=ventanaInformes)
b3 = Button(root, text="NOMINAS", width=10, command= ventanaNominas)

b.place(x=265, y=180, anchor=CENTER)
b1.place(x=350, y=180, anchor=CENTER)
b2.place(x=265, y=210, anchor=CENTER)
b3.place(x=350, y=210, anchor=CENTER)

labelTitulito = Label(root, text="¡Bienvenido Botarate!")
labelTitulito.pack(anchor=CENTER)
labelTitulito.config(fg="white",    # Foreground
             bg="black",   # Background
             font=("Corbel Light",14,
              )) 

labelTitulito.place(x=220, y=250)



root.mainloop()