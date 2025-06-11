import tkinter as tk
from tkinter import messagebox
from services.mi_sql import conectar
from views.dashboard import ventana_usuario

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="#f0f0f0",  # Color de fondo más suave
        padx=20,
        pady=20,
        width=400,  # Ancho más adecuado para un formulario
        height=400,
    )
    login_panel.pack_propagate(False)  # Evita que el frame se ajuste al contenido

    # Contenedor principal para centrar el formulario
    form_container = tk.Frame(login_panel, bg="#f0f0f0")
    form_container.pack(expand=True)

    # Título con mejor estilo
    titulo = tk.Label(
        form_container, 
        text="Inicio de Sesión", 
        font=("Arial", 20, "bold"), 
        bg="#f0f0f0",
        fg="#333333"
    )
    titulo.pack(pady=(0, 20))

    # Frame para los campos del formulario
    campos_frame = tk.Frame(form_container, bg="#f0f0f0")
    campos_frame.pack()

    # Estilo común para las etiquetas
    label_style = {"font": ("Arial", 10), "bg": "#f0f0f0", "fg": "#555555", "anchor": "w"}

    # Entrada correo
    tk.Label(campos_frame, text="Correo electrónico", **label_style).pack(fill="x", pady=(5, 0))
    entrada_correo = tk.Entry(
        campos_frame, 
        font=("Arial", 12),
        bg="white",
        relief="flat",
        highlightthickness=1,
        highlightcolor="#cccccc",
        highlightbackground="#cccccc"
    )
    entrada_correo.pack(fill="x", pady=(0, 15), ipady=5)

    # Entrada contraseña
    tk.Label(campos_frame, text="Contraseña", **label_style).pack(fill="x", pady=(5, 0))
    entrada_contrasenna = tk.Entry(
        campos_frame, 
        font=("Arial", 12),
        bg="white",
        show="*",  # Oculta la contraseña
        relief="flat",
        highlightthickness=1,
        highlightcolor="#cccccc",
        highlightbackground="#cccccc"
    )
    entrada_contrasenna.pack(fill="x", pady=(0, 20), ipady=5)

    # Botón ingresar con mejor estilo
    def funcion_boton():
        correo = entrada_correo.get()
        contrasenna = entrada_contrasenna.get()
        
        # Validación básica
        if not correo or not contrasenna:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
            
        try:
            consultar_usuario = conectar(f"SELECT * FROM usuario WHERE correo = '{correo}' AND contrasenna = '{contrasenna}'")

            if len(consultar_usuario) != 0:
                messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
                ventana.destroy()
                ventana_usuario(consultar_usuario)
            else:
                messagebox.showerror("Error", "Correo o contraseña incorrectos")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    boton = tk.Button(
        form_container, 
        text="Continuar", 
        command=funcion_boton,
        bg="#4CAF50",  # Color verde moderno
        fg="white",
        font=("Arial", 12, "bold"),
        relief="flat",
        padx=20,
        pady=10,
        activebackground="#45a049"
    )
    boton.pack(fill="x", pady=(10, 0))

    # Mensaje de pie de página
    footer = tk.Label(
        login_panel, 
        text="© 2023 Mi Aplicación. Todos los derechos reservados.",
        font=("Arial", 8),
        bg="#f0f0f0",
        fg="#999999"
    )
    footer.pack(side="bottom", pady=(20, 0))

    return login_panel