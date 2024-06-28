import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
import os
import time
import shutil
import numpy as np
from datetime import datetime

output_dir = os.path.dirname(os.path.abspath(__file__))

#INTERFAZ DEL SISTEMA
class LoginVentana(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Inicio de Sesión")
        self.geometry("250x150")
        self.center_window()  # Center the window
        self.label_usuario = tk.Label(self, text="Usuario:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack()
        self.label_contraseña = tk.Label(self, text="Contraseña:")
        self.label_contraseña.pack()
        self.entry_contraseña = tk.Entry(self, show="*")
        self.entry_contraseña.pack()
        self.button_login = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.button_login.pack()

    def iniciar_sesion(self):
        credenciales = {"usuario1": "1234", "usuario2": "contraseña2", "usuario3": "contraseña3"}
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        if credenciales.get(usuario) == contraseña:
            messagebox.showinfo("Inicio de Sesión", f"Inicio de sesión exitoso como {usuario}.")
            self.destroy()
            app = Interfaz(root)
            root.geometry("430x160")
            app.pack(expand=True, fill='both')
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Inténtalo de nuevo.")

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('+{}+{}'.format(x, y))

class Interfaz(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        frame_texto = tk.Frame(self)
        frame_texto.pack(expand=True, fill='both', side="left")

        tk.Label(frame_texto, text="Tomar fotografias", font=("Arial", 12)).pack(pady=(10, 5))
        tk.Label(frame_texto, text="Descarga de la Fotografia final", font=("Arial", 13)).pack()

        frame_botones = tk.Frame(self)
        frame_botones.pack(expand=True, fill='both', side="right")

        tk.Button(frame_botones, text="Tomar fotos", font=("Arial",11), command=self.conectar_camara).pack(pady=(10, 5), padx=10, ipadx=10, ipady=5)
        # tk.Button(frame_botones, text="Descargar foto final", font=("Arial", 11), command=self.descargar_foto_combinada).pack(pady=5, padx=10, ipadx=10, ipady=5)
        tk.Button(frame_botones, text="Ventana siguiente", font=("Arial", 11), command=self.mostrar_ventana_extra).pack(pady=5, padx=10, ipadx=10, ipady=5)

# LOGICA PARA LA CAPTURA DE FOTOS    
    def capturar_10_fotos(self):
        cap = cv2.VideoCapture(0)
        fotos = []
        for _ in range(10):
            time.sleep(180)  # Espera 1 segundo entre cada captura
            ret, frame = cap.read()
            if ret:
                fotos.append(frame)
            else:
                print("Error al capturar la foto.")
        cap.release()
        return fotos

    def guardar_fotos(self, fotos, carpeta):
        os.makedirs(carpeta, exist_ok=True)
        [cv2.imwrite(f'{carpeta}/foto_{i}.jpg', foto) for i, foto in enumerate(fotos)]

    def combinar_fotos(self, carpeta_base=None):
        if not carpeta_base:
            carpeta_base = self.obtener_ultima_carpeta()
            if not carpeta_base:
                print("No se encontraron carpetas de fotos.")
                return
        imagenes = [cv2.imread(os.path.join(carpeta_base, f'foto_{i}.jpg')) for i in range(10)]
        combined_image = np.vstack([np.hstack(imagenes[:5]), np.hstack(imagenes[5:])])
        output_path = os.path.join(carpeta_base, 'foto_combinada.jpg')
        cv2.imwrite(output_path, combined_image)
        print(f'Fotos combinadas y guardadas como {output_path}')
        return carpeta_base

    def obtener_ultima_carpeta(self):
        carpetas = [f.path for f in os.scandir(output_dir) if f.is_dir()]
        carpetas.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return carpetas[0] if carpetas else None

    def conectar_camara(self):
        fotos = self.capturar_10_fotos()
        carpeta_base = os.path.join(output_dir, datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        self.guardar_fotos(fotos, carpeta_base)
        print("Fotografias tomadas y guardadas en:", carpeta_base)
        carpeta_base = self.combinar_fotos(carpeta_base)
        messagebox.showinfo("Acción completada", "Fotografías tomadas y combinadas correctamente.")

    # Función descargar_foto_combinada eliminada

    def mostrar_ventana_extra(self):
        ventana_extra = tk.Toplevel(self.master)
        ventana_extra.title("Ventana Extra")
        ventana_extra.geometry("250x150")
        tk.Button(ventana_extra, text="Seleccionar y Descargar Foto", command=self.seleccionar_descargar_foto).pack(pady=10)

    def seleccionar_descargar_foto(self):
        carpeta_base = self.obtener_ultima_carpeta()
        if not carpeta_base:
            messagebox.showerror("Error", "No se encontraron carpetas de fotos.")
            return

        ruta_foto = filedialog.askopenfilename(initialdir=carpeta_base, title="Seleccionar Foto", filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
        if ruta_foto:
            nombre_foto = os.path.basename(ruta_foto)
            destino = os.path.join(os.path.expanduser("~"), "Downloads", nombre_foto)
            shutil.copy(ruta_foto, destino)
            messagebox.showinfo("Éxito", f"Foto '{nombre_foto}' descargada correctamente.")

root = tk.Tk()
root.title("BioVision")
login_window = LoginVentana(root)
root.mainloop()

