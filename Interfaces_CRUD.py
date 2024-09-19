from tkinter import ttk 
import tkinter as tk   # Normal Tkinter.* widgets are not themed!
from tkinter import *
from tkinter import messagebox as mensaje
from acciones_BBDD import *
from utilidades import Salir,borrar_campos
from plantilla_datos import plantilla_interfaz


def interfaz_comun(window):
    root= tk.Toplevel(window)
    
    # Frame concreto para esta ventana
    frame = ttk.Frame(root, width=400, height=400)
    frame.pack()
    
    barra_menu=tk.Menu(root)
    menu_BBDD=tk.Menu(barra_menu,tearoff=False)
    menu_BBDD.add_command(label="Salir",command=lambda: Salir(window))
    barra_menu.add_cascade(menu=menu_BBDD,label="BBDD")
    
    menu_Borrar=tk.Menu(barra_menu,tearoff=False)
    menu_Borrar.add_command(label="Borrar Campos",command=lambda: borrar_campos(frame))
    barra_menu.add_cascade(menu= menu_Borrar,label="Borrar")
    
    menu_CRUD=tk.Menu(barra_menu,tearoff=False)
    menu_CRUD.add_command(label="Crear",command=lambda: interfaz_crear_usuario(root))
    menu_CRUD.add_command(label="Borrar",command= lambda: interfaz_buscar_usuario(root,"Borrar"))
    menu_CRUD.add_command(label="Actualizar",command= lambda: interfaz_buscar_usuario(root,"Actualizar"))
    menu_CRUD.add_command(label="Leer",command= lambda:interfaz_buscar_usuario(root,"Leer"))
    menu_CRUD.add_command(label="Descargar todos",command= lambda:descargar_datos_usuario())
    barra_menu.add_cascade(menu=menu_CRUD,label="CRUD")
    
    menu_Ayuda=tk.Menu(barra_menu,tearoff=False)
    menu_Ayuda.add_command(label="Licencia")
    menu_Ayuda.add_command(label="Funciones")
    barra_menu.add_cascade(menu=menu_Ayuda,label="Ayuda")
    
    root.config(menu=barra_menu)
    
    return root,frame


def interfaz_buscar_usuario(window,accion):
    
    [root,frame]=interfaz_comun(window)
    id = StringVar()
    ttk.Label(frame, text=f"{accion} Usuario").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(frame, text="Id").grid(row=1, column=0, padx=5, pady=5)
    id_entry = ttk.Entry(frame, textvariable=id)
    id_entry.grid(row=1, column=4, padx=5, pady=5)
    if accion == "Actualizar":
        ttk.Button(frame, text="Buscar", command=lambda: interfaz_actualizar_usuario(root,id)).grid(row=2, column=2, padx=5, pady=5)
    elif accion == "Borrar":
        ttk.Button(frame, text="Buscar", command=lambda: interfaz_borrar_usuario(root,id)).grid(row=2, column=2, padx=5, pady=5) 
    else:
        ttk.Button(frame, text="Buscar", command=lambda: interfaz_leer_usuario(root,id)).grid(row=2, column=2, padx=5, pady=5)
        
    root.mainloop()

def interfaz_crear_usuario(window):
    
    [root,frame]=interfaz_comun(window)
    
    plantilla=plantilla_interfaz(frame,"normal")
    plantilla.rellenar_boton("crear")
    root.mainloop()
   
def interfaz_actualizar_usuario(window,id):
   
    resultado=id_user(id)
    if(resultado):
        [root,frame]=interfaz_comun(window)
        plantilla=plantilla_interfaz(frame,"normal")
        plantilla.rellenar_datos(resultado)
        plantilla.rellenar_boton("actualizar")
        
        root.mainloop()
    else:
        mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
        
   
def interfaz_borrar_usuario(window,id):
    resultado=id_user(id)
    if(resultado):
        
        [root,frame]=interfaz_comun(window)
        plantilla=plantilla_interfaz(frame,"normal")
        plantilla.rellenar_datos(resultado)
        plantilla.rellenar_boton("borrar")
       
        root.mainloop()
    else:
         mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
   

def interfaz_leer_usuario(window,id):
    
    resultado=id_user(id)
    
    if(resultado):
        
        [root,frame]=interfaz_comun(window)
        plantilla=plantilla_interfaz(frame,"disabled")
        plantilla.rellenar_datos(resultado)
        
        
        root.mainloop()
    else:
        mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
            
    

