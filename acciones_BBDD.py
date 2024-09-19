import csv
from sqlite3 import *
from utilidades import conectarBBDD,desconectarBBDD
from tkinter import messagebox as mensaje

def create_user(*args):
    tupla=(args[0].get(),args[1].get(),args[2].get(),args[3].get(),args[4].get())
    conn=conectarBBDD()
    resultado=conn[1].execute("INSERT INTO USUARIOS(username,password,nombre,apellido,direccion) VALUES(?,?,?,?,?)",tupla)
    conn[0].commit()
    desconectarBBDD(conn[0],conn[1])
    if resultado == None: mensaje.showerror("Datos Creacion","No se ha podido crear el usuario")
    else: mensaje.showinfo("Datos Creacion",f"Se ha creado el usuario con nombre: {args[2].get()}")
    
def descargar_datos_usuario():
    conn=conectarBBDD()
    prueba=conn[1].execute("SELECT * FROM USUARIOS")
    resultado=prueba.fetchall()
    desconectarBBDD(conn[0],conn[1])
    if(resultado!= None):
        with open("usuarios.csv","w",newline="") as File:
            writer = csv.writer(File)
            writer.writerows(resultado)
            mensaje.showinfo("Datos Creacion","Se ha descargado documento con todos los usuarios")
    else:
        mensaje.showinfo("AVISO","No hay usuarios guardados en la BBDD") 
def id_user(*args):
    
    id=args[0].get()
    conn=conectarBBDD()
    prueba=conn[1].execute("SELECT * FROM USUARIOS WHERE ID=?",id)
    resultado=prueba.fetchone()
    desconectarBBDD(conn[0],conn[1])
    if(resultado== None):
        return False
    else:
        return resultado
    
def actualizar_user(id,*args):
    resultado=comprobar_campos(*args)
    
    if not resultado :
        tupla=(args[0].get(),args[1].get(),args[2].get(),args[3].get(),args[4].get(),id)
        conn=conectarBBDD()
        prueba=conn[1].execute("Update USUARIOS set username=?,password=?,nombre=?,apellido=?,direccion=? where id=?",tupla)
        conn[0].commit()
        desconectarBBDD(conn[0],conn[1])
        mensaje.showinfo("Campos actualizados","Se han actualizado los campos")
    else:
        mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    
def borrar_user(id):
    
    if id is not None :
        
        conn=conectarBBDD()
        conn[1].execute("DELETE FROM USUARIOS where id=?",str(id))
        conn[0].commit()
        desconectarBBDD(conn[0],conn[1])
        mensaje.showinfo("Campos eliminados","Se ha borrado usuario")
    else:
        mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    
def comprobar_campos(*args):
    valor_vacio=False
    for campo in args:
        if(campo.get() is "" and type(campo) is "tkinter.StringVar"):
            valor_vacio=True
    
    return valor_vacio

def crear_usuario(*args):
    resultado=comprobar_campos(*args)
    
    if resultado: mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    else: create_user(*args)   
    
    
   
    