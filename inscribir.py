
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:56:21 2022

@author: Jose Manuel Gordon Alonso
"""
#definimos las pantallas
from tkinter import *
from tkinter import ttk, Label, Entry

from pip._internal.commands.list import format_for_columns


def ventanaAlta():
    def insertar():
        con=sqlite3.connect("empresa.db")
        cur=con.cursor()
        cur.execute("INSERT INTO EMPLEADOS values("+str(cod.get())+"','"
                                                  +nom.get()+"','"
                                                  +fechaAlta.get()+"','"
                                                  +fechaBaja.get()+"' null,'"
                                                  +dir.get()+"','"
                                                  +nif.get()+"','"
                                                  +iban.get()+"','"
                                                  +numSS.get()+"','"
                                                  +gen.get()+"','"
                                                  +dep.get()+"','"
                                                  +puesto.get()+"','"
                                                  +telf.get()+"','"
                                                  +str(sm.get())+"','"
                                                  +str(PagExtra.get())+"','"
                                                  +str(irpf.get())+"','"
                                                  +email.get()+"','"
                                                  +str(SS.get())+");"
                        )
        con.commit()
        cur.close()
        con.close()



    pantalla = Toplevel()
    pantalla.config(bd=15)
    pantalla.resizable(0, 0)
    pantalla.iconbitmap("descarga.ico")
    pantalla.title("Ventana de Alta")
    pantalla.configure(background="#76b5c5")
    pantalla.geometry('1000x800+300+500')
    #variables
    cod= IntVar()
    nom=StringVar()
    fechaAlta=StringVar()
    fechaBaja=StringVar()
    dir=StringVar()
    nif=StringVar()
    iban=StringVar()
    numSS=StringVar()
    gen=StringVar()
    dep=StringVar()
    puesto=StringVar()
    telf=StringVar()
    sm=DoubleVar()
    irpf=DoubleVar()
    email=StringVar()
    SS=DoubleVar()
    PagExtra=IntVar()

    #etiquetaCodigo empleado
    labelCodigoEmpleado=Label(pantalla, text="Codigo", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryCodigoEmpleado= Entry(pantalla, textvariable=cod, width=10)
    labelCodigoEmpleado.grid(row=0, column=0)
    entryCodigoEmpleado.grid(row=1, column=0)
    #etiquetapaisano
    labelApeellidosyNombre = Label(pantalla, text="Apellidos Nombre", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryApeellidosyNombre = Entry(pantalla, textvariable=nom, width=50)
    labelApeellidosyNombre.grid(row=0, column=1, columnspan=9)
    entryApeellidosyNombre.grid(row=1, column=1, columnspan=9 )
    #etiquetasdefechas
    labelFechaAlta=Label(pantalla, text="Fecha Alta", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryFechaAlta=Entry(pantalla, textvariable=fechaAlta, width=15)
    labelFechaAlta.grid(row=3, column=0)
    entryFechaAlta.grid(row=4, column=0)
    labelFechaBaja= Label(pantalla, text="Fecha Baja", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryFechaBaja= Entry(pantalla, textvariable= fechaBaja, width=15)
    labelFechaBaja.grid(row=3, column=1)
    entryFechaBaja.grid(row=4, column=1)
    labeldireccion = Label(pantalla, text="Direccion", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entrydirecion= Entry(pantalla, textvariable=dir,width=50)
    #etiquetadirecion
    labeldireccion.grid(row=3, column=3, columnspan=6, )
    entrydirecion.grid(row=4, column=3, columnspan=6, )
    #datospasisanoyAAPP
    labelNIF= Label(pantalla, text="NIF", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryNIF= Entry(pantalla, textvariable=nif, width=15)
    labelNIF.grid(row=5, column=0)
    entryNIF.grid(row=6, column=0)
    labelDatosBancarios= Label(pantalla, text="Datos Bancarios", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryDatosBancarios= Entry(pantalla, textvariable=iban, width=20)
    labelDatosBancarios.grid(row=5, column=1)
    entryDatosBancarios.grid(row=6, column=1)
    labelnumSS= Label(pantalla, text="Numero de Afilición SS", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entrynumSS= Entry(pantalla, textvariable=numSS, width=20)
    labelnumSS.grid(row=5, column=3)
    entrynumSS.grid(row=6, column=3)
    #otrosdatos
    labelGenero=Label(pantalla, text="Genero", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryGenero=Entry(pantalla, textvariable=gen, width=10)
    labelGenero.grid(row=7, column=0)
    entryGenero.grid(row=8, column=0)
    labelDeparatamento=Label(pantalla, text="Departamento", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryDepartamento=Entry(pantalla, textvariable=dep, width=20)
    labelDeparatamento.grid(row=7, column=1)
    entryDepartamento.grid(row=8, column=1)
    labelPuesto= Label(pantalla, text="Puesto", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryPuestos= Entry(pantalla, textvariable=puesto, width=20)
    labelPuesto.grid(row=7, column=3)
    entryPuestos.grid(row=8, column=3)
    #telefono
    labelTelefono= Label(pantalla, text="Telefono", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryTelefono= Entry(pantalla, textvariable=telf,width=15)
    labelTelefono.grid(row=9, column=0)
    entryTelefono.grid(row=9, column=1)
    labelsalariom= Label(pantalla, text="Salario Mensual", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entrysalario=  Entry(pantalla, textvariable=sm, width=15)
    labelsalariom.grid(row=9, column=2)
    entrysalario.grid(row=9, column=3)
    labelIRPF=Label(pantalla, text="IRPF", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryIrpf= Entry(pantalla, textvariable=irpf, width=20)
    labelIRPF.grid(row=9, column=5)
    entryIrpf.grid(row=9, column=6)
    #email
    labelemail= Label(pantalla, text="Email", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryEmail= Entry(pantalla, textvariable=email, width=20)
    labelemail.grid(row=10, column=0)
    entryEmail.grid(row=10, column=1, pady=10)
    labelPagasExtras= Label(pantalla, text="Pagas Extras", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryPagasExtars=Entry(pantalla,textvariable=PagExtra, width=20)
    labelPagasExtras.grid(row=10, column=3)
    entryPagasExtars.grid(row=10, column=4)
    labelSS= Label(pantalla, text="Seg. Social", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entrySS= Entry(pantalla, textvariable=SS, width=20)
    labelSS.grid(row=10, column=5)
    entrySS.grid(row=10, column=6)
    #boton
    botonInsertar=Button(pantalla, text="INSERTAR", font="Arial 14 bold", background="#b97455", fg="#e5eff0")
    botonInsertar.grid(row=11, column=5)
    #mensajevalidacion
    entryvalidacion= Entry(pantalla, width=70)
    entryvalidacion.grid(row=11, column=0, columnspan=4, ipady=13)

    
    pantalla.mainloop()








