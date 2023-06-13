from tkinter import *
from tkinter import ttk, Label, Entry
import sqlite3
from pip._internal.commands.list import format_for_columns

def ventanaInformes():
    def calculosBBDD():
        con=sqlite3.connect("empresa.db")
        cur=con.cursor()
        cur.execute("SELECT count(*) from empleados WHERE genero like 'Hombre'")
        hombresAlta=cur.fetchone()[0]
        cur.execute("SELECT count(*) from empleados WHERE genero like 'Mujeres'")
        mujeresAlta=cur.fetchone()[0]
        cur.execute("SELECT avg(salario) from empleados")
        retribucionmedia=cur.fetchone()[0]
        cur.execute("SELECT avg(salario) from empleados WHERE genero like 'Hombre'")
        hombresRetribucion=cur.fetchone()[0]
        cur.execute("SELECT avg(salario) from empleados WHERE genero like 'Mujeres'")
        mujeresRetribucion=cur.fetchone()[0]
        return
    def calcularMediaMujeres():
        porcmujeres=mujeresAlta/100
        return porcmujeres
    def calcularMediaHombres():
        porchombres=hombresAlta/100
        return porchombres
    
    pantallaInformes = Toplevel()
    pantallaInformes.config(bd=15)
    pantallaInformes.resizable(0, 0)
    pantallaInformes.iconbitmap("descarga.ico")
    pantallaInformes.title("Informes")
    pantallaInformes.configure(background="#F0C0A4")
    pantallaInformes.geometry('700x700+300+500')
    #Variables
    totalEmpleados=IntVar()
    totalEmpleadosBaja=IntVar()
    totalEdades=IntVar()
    retribucionmedia=DoubleVar()
    mujeresAlta=DoubleVar()
    mujeresBaja=DoubleVar()
    mujeresEdad=DoubleVar()
    mujeresRetribucion=DoubleVar()
    hombresAlta=DoubleVar()
    hombresBaja=DoubleVar()
    hombresEdad=DoubleVar()
    hombresRetribucion=DoubleVar()
    #titulo
    labelEmpleadosAlta=Label(pantallaInformes, text="EMPLEADO ALTA", padx=5, pady=5).grid(row=0, column=0)
    labelEmpleadosBaja=Label(pantallaInformes, text="EMPLEADOS BAJA", padx=5, pady=5).grid(row=0, column=1)
    labelMediaBaja=Label(pantallaInformes,text="MEDIA EDADES", padx=5, pady=5).grid(row=0,column=2)
    labelRetribucionMedia= Label(pantallaInformes, text="RETRIBUCION MEDIA",padx=5, pady=5).grid(row=0, column=3)

    entryRow11= Entry(pantallaInformes, textvariable=totalEmpleados,  width=10, state=DISABLED).grid(row=1,column=0)
    entryRow12= Entry(pantallaInformes, textvariable=totalEmpleadosBaja, width=10, state=DISABLED).grid(row=1,column=1)
    entryRow13= Entry(pantallaInformes, textvariable=totalEdades, width=10, state=DISABLED).grid(row=1,column=2)
    entryRow14= Entry(pantallaInformes, textvariable=retribucionmedia,width=10, state=DISABLED).grid(row=1,column=3)
    
    labelM= Label(pantallaInformes, text="% MUJERES", padx=5, pady=5).grid(row=2, column=0)
    labelM2= Label(pantallaInformes, text="% MUJERES",padx=5, pady=5).grid(row=2,column=1)
    labelM3= Label(pantallaInformes, text="MUJERES", padx=5, pady=5).grid(row=2,column=2)
    labelM4= Label(pantallaInformes, text="MUJERES", fg="BLUE", padx=5, pady=5).grid(row=2,column=3)

    entryRow31= Entry(pantallaInformes, textvariable=mujeresAlta, width=10, state=DISABLED).grid(row=3,column=0)
    entryRow32= Entry(pantallaInformes, textvariable=mujeresBaja, textvariable=mujeresAlta,width=10, state=DISABLED).grid(row=3,column=1)
    entryRow33= Entry(pantallaInformes, textvariable=mujeresEdad,width=10, state=DISABLED).grid(row=3,column=2)
    entryRow34= Entry(pantallaInformes, textvariable=mujeresRetribucion,width=10, state=DISABLED).grid(row=3,column=3)

    labelH= Label(pantallaInformes, text="% HOMBRES", padx=5, pady=5 ).grid(row=4,column=0)
    labelH2= Label(pantallaInformes, text="% HOMBRES", padx=5, pady=5).grid(row=4,column=1)
    labelH3= Label(pantallaInformes, text="HOMBRES", padx=5, pady=5).grid(row=4,column=2)
    labelH4= Label(pantallaInformes, text="HOMBRES",  fg="BLUE", padx=5, pady=5).grid(row=4,column=3)

    entryRow41= Entry(pantallaInformes, textvariable=hombresAlta, width=10, state=DISABLED).grid(row=5,column=0)
    entryRow42= Entry(pantallaInformes, textvariable=hombresBaja, width=10, state=DISABLED).grid(row=5,column=1)
    entryRow43= Entry(pantallaInformes, textvariable=hombresEdad, width=10, state=DISABLED).grid(row=5,column=2)
    entryRow44= Entry(pantallaInformes, textvariable=hombresRetribucion, width=10, state=DISABLED).grid(row=5,column=3)

    ventanaInformes.mainloop()