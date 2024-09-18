from tkinter import ttk 
import tkinter as tk   # Normal Tkinter.* widgets are not themed!
from tkinter import *
from tkinter import messagebox as mensaje
from acciones_BBDD import *
from tkinter import filedialog


def interfaz_comun(window):
    root= tk.Toplevel(window)
    
    # Frame concreto para esta ventana
    frame = ttk.Frame(root, width=400, height=400)
    frame.pack()
    
    barra_menu=tk.Menu(root)
    menu_BBDD=tk.Menu(barra_menu,tearoff=False)
    menu_BBDD.add_command(label="Conectar",command=lambda: abrir_archivo())
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
    barra_menu.add_cascade(menu=menu_CRUD,label="CRUD")
    
    menu_Ayuda=tk.Menu(barra_menu,tearoff=False)
    menu_Ayuda.add_command(label="Licencia")
    menu_Ayuda.add_command(label="Funciones")
    barra_menu.add_cascade(menu=menu_Ayuda,label="Ayuda")
    
    root.config(menu=barra_menu)
    
    return root,frame

#Recordando JS he buscado como encontrar los nodos hijos del frame para poder borrar los campos
def borrar_campos(frame):
    
    hijos = frame.winfo_children()
    for hijo in hijos:
        if isinstance(hijo, ttk.Entry):
            hijo.delete(0,END)

def Salir(window):
    window.destroy()

def interfaz_crear_usuario(window):
    
    #Desestructurazion para ahorra codigo
    [root,frame]=interfaz_comun(window)
    
    # Creamos textVariables
    nombre = StringVar()
    username = StringVar()
    password = StringVar()
    apellido = StringVar()
    direccion = StringVar()
    
    ttk.Label(frame, text="Crear Usuario").grid(row=0, column=2, padx=5, pady=5)
    ttk.Label(frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
    nombre_entry = ttk.Entry(frame, textvariable=nombre)
    nombre_entry.grid(row=1, column=4, padx=5, pady=5)
    ttk.Label(frame, text="Username").grid(row=2, column=0, padx=5, pady=5)
    user_entry = ttk.Entry(frame, textvariable=username)
    user_entry.grid(row=2, column=4, padx=5, pady=5)
    ttk.Label(frame, text="Password").grid(row=3, column=0, padx=5, pady=5)
    pass_entry = ttk.Entry(frame, textvariable=password, show="*")
    pass_entry.grid(row=3, column=4, padx=5, pady=5)
    ttk.Label(frame, text="Apellido").grid(row=4, column=0, padx=5, pady=5)
    apellido_entry = ttk.Entry(frame, textvariable=apellido)
    apellido_entry.grid(row=4, column=4, padx=5, pady=5)
    ttk.Label(frame, text="Direccion").grid(row=5, column=0, padx=5, pady=5)
    direccion_entry = ttk.Entry(frame, textvariable=direccion)
    direccion_entry.grid(row=5, column=4, padx=5, pady=5)
    
    ttk.Button(frame, text="Crear", command=lambda: crear_usuario(username, password,nombre, apellido, direccion)).grid(row=6, column=2, padx=5, pady=5)
    
    root.mainloop()
   
def interfaz_actualizar_usuario(window,id):
    
    #Desestructurazion para ahorra codigo
   
    resultado=id_user(id)
    
    if(resultado):
        
        [root,frame]=interfaz_comun(window)
        # Creamos textVariables
       
        username = StringVar(value=resultado[1])
        password = StringVar(value=resultado[2])
        nombre = StringVar(value=resultado[3])
        apellido = StringVar(value=resultado[4])
        direccion = StringVar(value=resultado[5])
        
        ttk.Label(frame, text="Crear Usuario").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = ttk.Entry(frame, textvariable=nombre)
        nombre_entry.grid(row=1, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Username").grid(row=2, column=0, padx=5, pady=5)
        user_entry = ttk.Entry(frame, textvariable=username)
        user_entry.grid(row=2, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Password").grid(row=3, column=0, padx=5, pady=5)
        pass_entry = ttk.Entry(frame, textvariable=password, show="*")
        pass_entry.grid(row=3, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Apellido").grid(row=4, column=0, padx=5, pady=5)
        apellido_entry = ttk.Entry(frame, textvariable=apellido)
        apellido_entry.grid(row=4, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Direccion").grid(row=5, column=0, padx=5, pady=5)
        direccion_entry = ttk.Entry(frame, textvariable=direccion)
        direccion_entry.grid(row=5, column=4, padx=5, pady=5)
        
        ttk.Button(frame, text="Actualizar", command=lambda: actualizar_user(username, password,nombre, apellido, direccion,id)).grid(row=6, column=2, padx=5, pady=5)
        
        root.mainloop()
    else:
        mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
        
def interfaz_buscar_usuario(window,accion):
    
    
    #Desestructurazion para ahorra codigo
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

   
def interfaz_borrar_usuario(window,id):
    
    resultado=id_user(id)
    
    if(resultado):
        
        [root,frame]=interfaz_comun(window)
        # Creamos textVariables
        username = StringVar(value=resultado[1])
        password = StringVar(value=resultado[2])
        nombre = StringVar(value=resultado[3])
        apellido = StringVar(value=resultado[4])
        direccion = StringVar(value=resultado[5])
        
        ttk.Label(frame, text="Crear Usuario").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = ttk.Entry(frame, textvariable=nombre)
        nombre_entry.grid(row=1, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Username").grid(row=2, column=0, padx=5, pady=5)
        user_entry = ttk.Entry(frame, textvariable=username)
        user_entry.grid(row=2, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Password").grid(row=3, column=0, padx=5, pady=5)
        pass_entry = ttk.Entry(frame, textvariable=password, show="*")
        pass_entry.grid(row=3, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Apellido").grid(row=4, column=0, padx=5, pady=5)
        apellido_entry = ttk.Entry(frame, textvariable=apellido)
        apellido_entry.grid(row=4, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Direccion").grid(row=5, column=0, padx=5, pady=5)
        direccion_entry = ttk.Entry(frame, textvariable=direccion)
        direccion_entry.grid(row=5, column=4, padx=5, pady=5)
        
        ttk.Button(frame, text="Borrar", command=lambda: borrar_user(id)).grid(row=6, column=2, padx=5, pady=5)
        
        root.mainloop()
    else:
         mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
   

def interfaz_leer_usuario(window,id):
    
    resultado=id_user(id)
    
    if(resultado):
        
        [root,frame]=interfaz_comun(window)
        # Creamos textVariables
        username = StringVar(value=resultado[1])
        password = StringVar(value=resultado[2])
        nombre = StringVar(value=resultado[3])
        apellido = StringVar(value=resultado[4])
        direccion = StringVar(value=resultado[5])
        
        ttk.Label(frame, text="Crear Usuario").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = ttk.Entry(frame, textvariable=nombre,state=DISABLED)
        nombre_entry.grid(row=1, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Username").grid(row=2, column=0, padx=5, pady=5)
        user_entry = ttk.Entry(frame, textvariable=username,state=DISABLED)
        user_entry.grid(row=2, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Password").grid(row=3, column=0, padx=5, pady=5)
        pass_entry = ttk.Entry(frame, textvariable=password, show="*",state=DISABLED)
        pass_entry.grid(row=3, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Apellido").grid(row=4, column=0, padx=5, pady=5)
        apellido_entry = ttk.Entry(frame, textvariable=apellido,state=DISABLED)
        apellido_entry.grid(row=4, column=4, padx=5, pady=5)
        ttk.Label(frame, text="Direccion").grid(row=5, column=0, padx=5, pady=5)
        direccion_entry = ttk.Entry(frame, textvariable=direccion,state=DISABLED)
        direccion_entry.grid(row=5, column=4, padx=5, pady=5)
        
        
        root.mainloop()
    else:
        mensaje.showwarning("Id no encontrado","El id al que se hace referencia no existe")
            
def comprobar_campos(*args):
    valor_vacio=False
    for campo in args:
        if(campo.get() == ""):
            valor_vacio=True
    
    return valor_vacio


def crear_usuario(*args):
    resultado=comprobar_campos(*args)
    
    if resultado: mensaje.showwarning("Campo Incompleto","Se deben rellenar todos los campos")
    else: create_user(*args)
    
def abrir_archivo():
    # Abre un cuadro de diálogo para seleccionar un archivo
    file_path = filedialog.askopenfilename()
    if file_path:
        mensaje.showinfo("Archivo Seleccionado", f"Has seleccionado: {file_path}")
