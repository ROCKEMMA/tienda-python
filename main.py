import tkinter as tk
from views.header_view import cargar_header
from views.productos_view import cargar_productos
from views.login_view import cargar_login

ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")

# Configurar el grid para que los frames se expandan correctamente
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)

# Cargar los frames de login en columnas diferentes
frame_login1 = cargar_login(ventana)
frame_login1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

ventana.mainloop()