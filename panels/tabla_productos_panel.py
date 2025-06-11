# tabla_productos.py
import tkinter as tk
from tkinter import ttk

def cargar_productos(ventana):
    productos_panel = tk.Frame(
        ventana,
        bg="purple",
        padx=0,
        pady=0,
        width=1000,
        height=540,
    )
    productos_panel.pack()

    campos = ("ID", "Nombre", "Edad")
    datos = [
        (1, "Ana", 23),
        (2, "Luis", 30),
        (3, "María", 27),
        (4, "Pedro", 35)
    ]

    tabla = ttk.Treeview(productos_panel, columns=campos, show="headings")

    for campo in campos:
        tabla.heading(campo, text=campo)
        tabla.column(campo, anchor="center")

    for fila in datos:
        tabla.insert("", tk.END, values=fila)

    scroll = ttk.Scrollbar(productos_panel, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scroll.set)

    tabla.pack(side="left", expand=True, fill="both")
    scroll.pack(side="right", fill="y")

    print("panel productos cargado")

    return productos_panel