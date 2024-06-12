import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,scrolledtext

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Simple con Tkinter")
root.geometry('400x500')

# Etiqueta de bienvenida

# Funcion de subir
def subir_imagen():
    file_path=filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content =file.read()
            
        


# Botón para subir imagen
boton=ttk.Button(text="Subir imagen", command=subir_imagen)
boton.place(x=100,y=100)


# Ejecutar la aplicación
root.mainloop()
