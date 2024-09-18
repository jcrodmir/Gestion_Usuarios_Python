from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
import Opciones_CRUD as operaciones
from utilidades import *



def creacion_Interfaz_Inicial(nombre):
    #Principal
    window = ThemedTk(theme="itft1")
    window.geometry("400x400")
    #Frame
    frame=ttk.Frame(window,width=400,height=400)
    frame.grid()
    #Estilos botones
    s_button=ttk.Style()
    s_button.configure(".TButton",font=("Helvetica",20), padding=10)
    #Creación Label y Button con el nombre que llegue por parametro
    ttk.Label(text="Gestión de Usuarios",font=("Arial",20)).place(relx=0.5,rely=0.1,anchor="n")
    ttk.Button(frame,text=nombre,command=lambda : operaciones.interfaz(window),style=".TButton").place(relx=0.5, rely=0.5, anchor="center")
    window.mainloop()
    

def inicio_programa():
    #Creamos carpeta BBDD para la base de datos y tenerlo mejor estructurado.
    crearCarpetaBBDD()

    #Crea , conecta BBDD
    conn=conectarBBDD()
    #Seleccionamos dentro de squlite_master para ver si contiene la tabla usuario
    comprobarTabla= conn[1].execute("SELECT name FROM sqlite_master WHERE name='USUARIOS'")


    #Si la contiene se creara tabla y tendremos la interfaz con el boton crear, en caso contrario será conectar
    if comprobarTabla.fetchone() is None:
        conn[1].execute("CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,USERNAME VARCHAR(25), PASSWORD VARCHAR(20), NOMBRE VARCHAR(25),APELLIDO VARCHAR(50),DIRECCION VARCHAR(50))")
        creacion_Interfaz_Inicial("Crear")
        
    else: 
        creacion_Interfaz_Inicial("Conectar")
        
    #Cerramos conexion y cursor
    desconectarBBDD(conn[0],conn[1])

#Iniciamos Programa

inicio_programa()



