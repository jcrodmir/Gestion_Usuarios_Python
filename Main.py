from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import sqlite3 as sql

window = ThemedTk(theme="arc")


miConexion=sql.connect("BBDD/Gestion_Usuarios")
miCursor=miConexion.cursor()

comprobarTabla= miCursor.execute("SELECT name FROM sqlite_master WHERE name='USUARIOS'")


if comprobarTabla.fetchone() is None:
    ttk.Button(window,text="Crear").pack()
    miCursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE VARCHAR(25), APELLIDOS VARCHAR(40))")
    
else: 
    ttk.Button(window,text="Conectar").pack()
    
miCursor.close()
miConexion.close()
window.mainloop()