import sqlite3
conn = sqlite3.connect("ejemplo.db")
cursor = conn.cursor()
# Creamos la tabla de Direcciones
cursor.execute("CREATE TABLE usuarios (nombre TEXT, edad NUMERIC, email TEXT , dni TEXT)")
# Agregamos dos direcciones
#cursor.execute("INSERT INTO Direcciones VALUES ('Calle 1', 1644)")
#cursor.execute("INSERT INTO Direcciones VALUES ('Calle 2', 7594)")
#q = cursor.execute("SELECT calle, cp FROM Direcciones")
#for data in q.fetchall():
#    print("Calle: %s, Codigo Postal: %d" % (data[0], data[1]))
conn.commit()
cursor.close()
conn.close()