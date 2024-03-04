import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Login:")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)        
        self.login()

    def login(self):
        self.label1=ttk.Label(self.labelframe1, text="Nombre de usuario:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Ingrese clave:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe1, show="*")
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Ingresar",command=self.ingresar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def ingresar(self):
        self.ventana1.destroy()
        
def mostrar():
    aplicacion1=Aplicacion()