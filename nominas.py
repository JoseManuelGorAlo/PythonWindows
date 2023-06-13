
from tkinter import *
from pip._internal.commands.list import format_for_columns

def ventanaNominas():

    pantalla1= Toplevel()
    pantalla1.config(bd=15)
    pantalla1.resizable(0, 0)
    pantalla1.iconbitmap("descarga.ico")
    pantalla1.title("Ventana de Alta")
    pantalla1.configure(background="#76b5c5")
    pantalla1.geometry('1000x800+300+500')

    #variables
    CodigoEmpleado= StringVar()
    IrpfREtry= StringVar()

    #etiquetaCodigo empleado
    labelCodigoEmpleado=Label(pantalla1, text="Codigo", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryCodigoEmpleado= Entry(pantalla1, textvariable=CodigoEmpleado, width=10)
    labelCodigoEmpleado.grid(row=0, column=0)
    entryCodigoEmpleado.grid(row=1, column=0)

    #etiquetapaisano
    labelApeellidosyNombre = Label(pantalla1, text="Apellidos Nombre", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryApeellidosyNombre = Entry(pantalla1, width=50, state=DISABLED)
    labelApeellidosyNombre.grid(row=0, column=1, columnspan=9)
    entryApeellidosyNombre.grid(row=1, column=1, columnspan=9)

    #etiquetasdefechas
    labelFechaAlta=Label(pantalla1, text="Fecha Alta", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryFechaAlta=Entry(pantalla1, width=15,state=DISABLED)
    labelFechaAlta.grid(row=3, column=0)
    entryFechaAlta.grid(row=4, column=0)
    labelFechaBaja= Label(pantalla1, text="Fecha Baja", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryFechaBaja= Entry(pantalla1, width=15,state=DISABLED)
    labelFechaBaja.grid(row=3, column=1)
    entryFechaBaja.grid(row=4, column=1)
    labeldireccion = Label(pantalla1, text="Direccion", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")    
    entrydirecion= Entry(pantalla1, width=50,state=DISABLED)
    #etiquetadirecion
    labeldireccion.grid(row=3, column=3, columnspan=6, )
    entrydirecion.grid(row=4, column=3, columnspan=6, )

    #datospasisanoyAAPP
    labelNIF= Label(pantalla1, text="NIF", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryNIF= Entry(pantalla1, width=15,state=DISABLED)
    labelNIF.grid(row=5, column=0)
    entryNIF.grid(row=6, column=0)
    labelDatosBancarios= Label(pantalla1, text="Datos Bancarios", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryDatosBancarios= Entry(pantalla1, width=20, state=DISABLED)
    labelDatosBancarios.grid(row=5, column=1)
    entryDatosBancarios.grid(row=6, column=1)
    labelnumSS= Label(pantalla1, text="Numero de Afilición SS", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entrynumSS= Entry(pantalla1, width=20, state=DISABLED )
    labelnumSS.grid(row=5, column=3)
    entrynumSS.grid(row=6, column=3)

    #otrosdatos
    labelGenero=Label(pantalla1, text="Genero", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryGenero=Label(pantalla1, width=10, state=DISABLED)
    labelGenero.grid(row=7, column=0)
    entryGenero.grid(row=8, column=0)
    labelDeparatamento=Label(pantalla1, text="Departamento", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryDepartamento=Entry(pantalla1, width=20, state=DISABLED)
    labelDeparatamento.grid(row=7, column=1)
    entryDepartamento.grid(row=8, column=1)
    labelPuesto= Label(pantalla1, text="Puesto", font="Arial 11 bold", background="#76b5c5", fg="#e5eff0")
    entryPuestos= Entry(pantalla1, width=20, state=DISABLED)
    labelPuesto.grid(row=7, column=3)
    entryPuestos.grid(row=8, column=3)

    #telefono
    labelTelefono= Label(pantalla1, text="Telefono", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryTelefono= Entry(pantalla1, width=15, state=DISABLED)
    labelTelefono.grid(row=9, column=0)
    entryTelefono.grid(row=9, column=1)
    labelsalariom= Label(pantalla1, text="Salario Mensual", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entrysalario=  Entry(pantalla1, width=15)
    labelsalariom.grid(row=9, column=2)
    entrysalario.grid(row=9, column=3)
    labelIRPF=Label(pantalla1, text="IRPF", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryIrpf= Entry(pantalla1, width=20, state=DISABLED)
    labelIRPF.grid(row=9, column=5)
    entryIrpf.grid(row=9, column=6)
    labelIrpfREtry= Label(pantalla1, text="Retencion de IRPF", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    labelIrpfREtry.grid(row=9, column=7)
    entryIrpfREtry=Entry(pantalla1, textvariable= IrpfREtry, width=15)
    entryIrpfREtry.grid(row=9, column=8)

    #email
    labelemail= Label(pantalla1, text="Email", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryEmail= Entry(pantalla1,width=20, state=DISABLED)
    labelemail.grid(row=10, column=0)
    entryEmail.grid(row=10, column=1, pady=10)
    labelPagasExtras= Label(pantalla1, text="Pagas Extras", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entryPagasExtars=Entry(pantalla1,width=20)
    labelPagasExtras.grid(row=10, column=3)
    entryPagasExtars.grid(row=10, column=4)
    labelSS= Label(pantalla1, text="Seg. Social", font="Arial 9 bold", background="#76b5c5", fg="#e5eff0")
    entrySS= Entry(pantalla1, width=20, state=DISABLED)
    labelSS.grid(row=10, column=5)
    entrySS.grid(row=10, column=6)

    #boton
    botonInsertar=Button(pantalla1, text="INSERTAR", font="Arial 14 bold", background="#b97455", fg="#e5eff0")
    botonInsertar.grid(row=11, column=5)
    botonCargarEmpleado= Button(pantalla1, text="CARGAR EMPLEADO",font="Arial 14 bold", background="#b97455", fg="#e5eff0")
    botonCargarEmpleado.grid(row=12, column=0)
    botonCalcular= Button(pantalla1, text="CALCULAR",font="Arial 14 bold", background="#b97455", fg="#e5eff0")
    botonCalcular.grid(row=13, column=2)
    botonImprimir=Button(pantalla1, text="IMPRIMIR",font="Arial 14 bold", background="#b97455", fg="#e5eff0")
    botonImprimir.grid(row=12, column=3)

    #mensajevalidacion
    entryvalidacion= Entry(pantalla1, width=70)
    entryvalidacion.grid(row=11, column=0, columnspan=4, ipady=13)

    
    pantalla1.mainloop()