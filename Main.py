from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import sqlite3 as sql
import Opciones_CRUD as operaciones

window = ThemedTk(theme="arc")
window.geometry("400x400")
s_button=ttk.Style()
s_button.configure(".TButton",font=("Helvetica",20))

miConexion=sql.connect("BBDD/Gestion_Usuarios")
miCursor=miConexion.cursor()

comprobarTabla= miCursor.execute("SELECT name FROM sqlite_master WHERE name='USUARIOS'")


if comprobarTabla.fetchone() is None:
    boton=ttk.Button(window,text="Crear",command=lambda : operaciones.interfaz(),style=".TButton").pack(padx=10,pady=10)
    miCursor.execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR(25), PASSWORD VARCHAR(20), NOMBRE VARCHAR(25),DIRECCION VARCHAR(50), COMENTARIO TEXT(250))")
   
else: 
    ttk.Label(text="Gestión de Usuarios",font=("Arial",20)).place(relx=0.5,rely=0.1,anchor="n")
    boton=ttk.Button(window,text="Conectar",command=lambda : operaciones.interfaz(window),style=".TButton").place(relx=0.5, rely=0.5, anchor="center")
    
    
    
miCursor.close()
miConexion.close()
window.mainloop()
