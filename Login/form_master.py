from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk

# Definición de la clase Login
class Login:
    # Método de inicialización
    def __init__(self):
        # Usuarios predefinidos
        self.usuarios = {'admin': 'admin', 'usuario1': 'contraseña1', 'usuario2': 'contraseña2'}  
        
        # Configuración de la ventana
        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("INICIO DE SESIÓN")

        fondo = "#6b9867"

        # Frame superior
        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)

        # Frame inferior
        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)

        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        # Título
        self.titulo = Label(self.frame_superior,
                            text="LOGIN",
                            font=("calisto MT", 36, "bold"),
                            bg=fondo)
        self.titulo.pack(side="top", pady=20)
        
        # Carga de la imagen/logo
        self.img = Image.open("hongos.jpg")  # Cambiar la ruta a la ubicación de tu imagen
        self.img = self.img.resize((160, 165))  # Ajusta el tamaño de la imagen según sea necesario
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image=self.render, bg=fondo)
        self.fondo.pack(expand=True, fill="both", side="top")

        # Etiqueta de Usuario
        self.label_usuario = Label(self.frame_inferior,
                                   text="Usuario:",
                                   font=("Arial", 18),
                                   bg=fondo,
                                   fg="black")
        self.label_usuario.grid(row=0, column=0, padx=10, sticky="e")

        # Entry de Usuario
        self.entry_usuario = Entry(self.frame_inferior,
                                   bd=0,
                                   width=14,
                                   font=("Arial", 18))
        self.entry_usuario.grid(row=0, column=1, columnspan=3, padx=5, sticky="w")

        # Etiqueta de Contraseña
        self.label_contraseña = Label(self.frame_inferior,
                                      text="Contraseña:",
                                      font=("Arial", 18),
                                      bg=fondo,
                                      fg="black")
        self.label_contraseña.grid(row=1, column=0, padx=10, sticky="e")

        # Entry de Contraseña
        self.entry_contraseña = Entry(self.frame_inferior,
                                      bd=0,
                                      width=14,
                                      font=("Arial", 18),
                                      show="*")
        self.entry_contraseña.grid(row=1, column=1, columnspan=3, padx=5, sticky="w")

        # Botón Ingresar
        self.boton_ingresar = Button(self.frame_inferior,
                                     text="Ingresar",
                                     width=16,
                                     font=("Arial", 12),
                                     command=self.entrar)
        self.boton_ingresar.grid(row=2, column=0, columnspan=2, pady=35)

        # Botón Registrar
        self.boton_registrar = Button(self.frame_inferior,
                                      text="Registrar",
                                      width=16,
                                      font=("Arial", 12),
                                      command=self.registrar)
        self.boton_registrar.grid(row=2, column=2, columnspan=2, pady=35)

        mainloop()

    # Método para iniciar sesión
    def entrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()

        if nombre in self.usuarios and self.usuarios[nombre] == contra:
            messagebox.showinfo("Acceso correcto", "Has ingresado como {}".format(nombre))
        else:
            messagebox.showinfo("Acceso incorrecto", "Usuario o contraseña incorrectos")

    # Método para registrar un usuario
    def registrar(self):
        nombre = self.entry_usuario.get()
        contra = self.entry_contraseña.get()

        if nombre not in self.usuarios:
            self.usuarios[nombre] = contra
            messagebox.showinfo("Registro exitoso", "Usuario {} registrado correctamente".format(nombre))
        else:
            messagebox.showinfo("Error de registro", "El usuario {} ya existe".format(nombre))

# Instanciación de la clase Login
Login()
