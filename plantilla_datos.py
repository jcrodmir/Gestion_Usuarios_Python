from tkinter import ttk 
from tkinter import *
from acciones_BBDD import *

class plantilla_interfaz():
    
    def __init__(self,frame,estado) -> None:
        self.username = StringVar()
        self.password = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.direccion = StringVar()
        self.id=""
        self.frame=frame
        self.labels_entrys(estado)
        
    
    def rellenar_boton(self,tipo):
        
        if(tipo is "crear"): ttk.Button(self.frame, text="Crear", command=lambda: crear_usuario(self.username,self.password,self.nombre, self.apellido, self.direccion)).grid(row=6, column=2, padx=5, pady=5)
        elif(tipo is "actualizar"): ttk.Button(self.frame, text="Actualizar", command=lambda: actualizar_user(self.id,self.username,self.password,self.nombre, self.apellido, self.direccion)).grid(row=6, column=2, padx=5, pady=5)
        elif(tipo is "borrar"):  ttk.Button(self.frame, text="Borrar", command=lambda: borrar_user(self.id)).grid(row=6, column=2, padx=5, pady=5)
            
    
    def rellenar_datos(self,resultado):
        self.id=resultado[0]
        self.username.set(value=resultado[1])
        self.password.set(value=resultado[2])
        self.nombre.set(value=resultado[3])
        self.apellido.set(value=resultado[4])
        self.direccion.set(value=resultado[5])
        
        
    def labels_entrys(self,estado):
        ttk.Label(self.frame, text="Crear Usuario").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.frame, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
        nombre_entry = ttk.Entry(self.frame, textvariable=self.nombre,state=estado)
        nombre_entry.grid(row=1, column=4, padx=5, pady=5)
        ttk.Label(self.frame, text="Username").grid(row=2, column=0, padx=5, pady=5)
        user_entry = ttk.Entry(self.frame, textvariable=self.username,state=estado)
        user_entry.grid(row=2, column=4, padx=5, pady=5)
        ttk.Label(self.frame, text="Password").grid(row=3, column=0, padx=5, pady=5)
        pass_entry = ttk.Entry(self.frame, textvariable=self.password, show="*",state=estado)
        pass_entry.grid(row=3, column=4, padx=5, pady=5)
        ttk.Label(self.frame, text="Apellido").grid(row=4, column=0, padx=5, pady=5)
        apellido_entry = ttk.Entry(self.frame, textvariable=self.apellido,state=estado)
        apellido_entry.grid(row=4, column=4, padx=5, pady=5)
        ttk.Label(self.frame, text="Direccion").grid(row=5, column=0, padx=5, pady=5)
        direccion_entry = ttk.Entry(self.frame, textvariable=self.direccion,state=estado)
        direccion_entry.grid(row=5, column=4, padx=5, pady=5)