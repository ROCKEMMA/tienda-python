# dashboard.py

import tkinter as tk 
from components.tabla_productos import cargar_productos

def ventana_usuario(datos):
    venta_usuario = tk.Tk()
    venta_usuario.title("Ventana usuario")
    venta_usuario.geometry("1800x1000")

    # Aquí cargas el panel con la tabla
    cargar_productos(venta_usuario)

    venta_usuario.mainloop()
