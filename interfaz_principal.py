from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
import tkinter as tk
from ttkthemes import ThemedTk
from Interfaces_CRUD import *


def crear_botones(frame,window):
    ttk.Button(frame,text="Crear",command= lambda: interfaz_crear_usuario(window)).grid(row=1,column=1,pady=30,padx=50,ipady=10,ipadx=60)
    ttk.Button(frame,text="Leer",command= lambda:interfaz_buscar_usuario(window,"Leer")).grid(row=1,column=3,pady=30,padx=50,ipady=10,ipadx=60)
    ttk.Button(frame,text="Borrar",command= lambda: interfaz_buscar_usuario(window,"Borrar")).grid(row=3,column=1,pady=30,padx=50,ipady=10,ipadx=60)
    ttk.Button(frame,text="Actualizar",command= lambda: interfaz_buscar_usuario(window,"Actualizar")).grid(row=3,column=3,pady=30,padx=50,ipady=10,ipadx=50)
    
    
def interfaz(pantalla_inicial):
    #Destruimos la anterior ventana
    pantalla_inicial.destroy()
    #Creamos nueva interfaz
    window = ThemedTk(theme="itft1")
    #Frame concreto para esta ventana
    frame=ttk.Frame(window,width=400,height=400)
    frame.grid()
    #Creamos Botones para esta ventana
    crear_botones(frame,window)
    

    window.mainloop()

    

    