import os
import sqlite3 as sql

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