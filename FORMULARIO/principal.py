import tkinter as tk
from tkinter import ttk
import LOGIN.registro.login
import LOGIN.Util.codificacion


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("SISTEMA")
        
        self.boton2 = ttk.Button(self.ventana1, text=" BIENVENIDO!!,INICIA TU SESIÓN ", command=self.mostrar_login)
        self.boton2.grid(column=0, row=0)
        
        self.ventana1.mainloop()

    def mostrar_login(self):
        LOGIN.registro.login.mostrar()

aplicacion1 = Aplicacion()
