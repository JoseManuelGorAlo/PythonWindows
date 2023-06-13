from tkinter import *
from tkinter import ttk, Label, Entry

from pip._internal.commands.list import format_for_columns

def ventanaBajas():
    def actualizarBajaBBDD():
         con=sqlite3.connect("empresa.db")
         cur=con.cursor()
         cur.execute("UPDATE empleados set FechaBaja= '{} ' WHERE ID ='{}'").format(FechaBaja,CodEmpl)
         con.commit()
         con.close()

    pantallaBaja = Tk()
    pantallaBaja.config(bd=15)
    pantallaBaja.resizable(0, 0)
    pantallaBaja.iconbitmap("descarga.ico")
    pantallaBaja.title("Ventana de Bajas")
    pantallaBaja.configure(background="#C70C2B")
    pantallaBaja.geometry('700x700+300+500')
    #variables de los entrys// show='*' muestra solo el caracter que le digamos entre comillas
    CodEmpl= StringVar()
    FechaBaja= StringVar()
    validacion=StringVar()
    #comenzamos con los recuadritos
    labelCodigoEmpleado=Label(pantallaBaja,text="Codigo Empleado", font="Arial 15 bold", background="#76b5c5", fg="#7470FA").grid(row=0,column=0,pady=7)
    entryCodigoEmpleado=Entry(pantallaBaja, textvariable=CodEmpl, width=20).grid(row=1,column=0,sticky=EW)

    labelSeparacion=Label(pantallaBaja, text="",width=10,background="#C70C2B").grid(row=0,column=1)
    labelFechaBaja=Label(pantallaBaja,text="Fecha de Baja", font="Arial 15 bold", background="#76b5c5", fg="#7470FA").grid(row=0, column=2,pady=7)
    entryFechaBaja=Entry(pantallaBaja,textvariable=FechaBaja, width=20).grid(row=1,column=2,sticky=EW)
    #recuadrod de validacion
    entryvalidacion= Entry(pantallaBaja, textvariable=validacion, width=50)
    entryvalidacion.grid(row=2,column=1, ipady=13, pady=14)
    #boton de confirmar
    botondeConfirmar=Button(pantallaBaja,text="CONFIRMAR",font="Arial 14 bold",background="#b97455", fg="#e5eff0").grid(row=3,column=1)

    ventanaBajas.mainloop()