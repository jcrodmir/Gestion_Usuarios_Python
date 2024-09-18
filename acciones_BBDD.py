from sqlite3 import *
import utilidades as utills
from tkinter import messagebox as mensaje

def create_user(*args):
    tupla=(args[0].get(),args[1].get(),args[2].get(),args[3].get(),args[4].get())
    conn=utills.conectarBBDD()
    resultado=conn[1].execute("INSERT INTO USUARIOS(username,password,nombre,apellido,direccion) VALUES(?,?,?,?,?)",tupla)
    conn[0].commit()
    utills.desconectarBBDD(conn[0],conn[1])
    if resultado == None: mensaje.showerror("Datos Creacion","No se ha podido crear el usuario")
    else: mensaje.showinfo("Datos Creacion",f"Se ha creado el usuario con nombre: {args[2].get()}")
    
def id_user(*args):
    
    id=args[0].get()
    conn=utills.conectarBBDD()
    prueba=conn[1].execute("SELECT * FROM USUARIOS WHERE ID=?",id)
    resultado=prueba.fetchone()
    utills.desconectarBBDD(conn[0],conn[1])
    if(resultado== None):
        return False
    else:
        return resultado
    
def actualizar_user(*args):
    resultado=comprobar_campos(*args)
    
    if not resultado :
        tupla=(args[0].get(),args[1].get(),args[2].get(),args[3].get(),args[4].get(),args[5].get())
        conn=utills.conectarBBDD()
        prueba=conn[1].execute("Update USUARIOS set username=?,password=?,nombre=?,apellido=?,direccion=? where id=?",tupla)
        conn[0].commit()
        utills.desconectarBBDD(conn[0],conn[1])
    else:
        mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    
def borrar_user(*args):
    resultado=comprobar_campos(*args)
    if not resultado :
        
        id=args[0].get()
        conn=utills.conectarBBDD()
        prueba=conn[1].execute("DELETE FROM USUARIOS where id=?",id)
        conn[0].commit()
        utills.desconectarBBDD(conn[0],conn[1])
    else:
        mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    
def comprobar_campos(*args):
    valor_vacio=False
    for campo in args:
        if(campo.get() == ""):
            valor_vacio=True
    
    return valor_vacio

    
    
    
   
    