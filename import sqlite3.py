import sqlite3
con=sqlite3.connect("empresa.db")
cur=con.cursor()
cur.execute("create table empleados(codigo integer not null primaykey unique, nombre varchar(50), fechaInicio date, fechaFin date, direccion varchar(50), nif varchar(50), iban varchar(50), numeroSS varchar(50), genero varchar(50), departamento varchar(50), puesto varchar(50), telefono varchar(50), email varchar(50), salariomensual decimal, pagasExtra decimal, IRPF decimal, SSSS decimal)")
