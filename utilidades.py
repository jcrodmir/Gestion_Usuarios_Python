import os
import sqlite3 as sql
from tkinter import *
from tkinter import ttk

def crearCarpetaBBDD():
    ruta="./BBDD"
    if not os.path.exists(ruta):
        os.mkdir(ruta)

def conectarBBDD():
    miConexion=sql.connect("BBDD/Gestion_Usuarios")
    miCursor=miConexion.cursor()
    
    return (miConexion,miCursor)
    
def desconectarBBDD(miConexion,miCursor):
    #Cerramos conexion y cursor
    miCursor.close()
    miConexion.close()


#Recordando JS he buscado como encontrar los nodos hijos del frame para poder borrar los campos

def borrar_campos(frame):
    
    hijos = frame.winfo_children()
    for hijo in hijos:
        if isinstance(hijo, ttk.Entry):
            hijo.delete(0,END)

def Salir(window):
    window.destroy()
