import tkinter as tk
from services.mi_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="green",
        padx=0,
        pady=0,
        width=1000,
        height=600,
        )

    # Formulario
    titulo = tk.Label(login_panel, text="Login")
    titulo.pack()

    # Entrada correo
    txt_correo = tk.Label(login_panel, text="correo")
    txt_correo.pack()

    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

    # Entrada contraseña
    txt_contrasenna = tk.Label(login_panel, text="Contraseña")
    txt_contrasenna.pack()

    entrada_contrasenna = tk.Entry(login_panel)
    entrada_contrasenna.pack()

    # Boton ingresar
    def funcion_boton():
        correo = entrada_correo.get()
        cotrasenna = entrada_contrasenna.get()
        print(conectar(f"SELECT * FROM usuario WHERE correo = '{correo}'"))
        
    
    boton = tk.Button(login_panel, text="Continuar", command=funcion_boton)
    boton.pack()


    #login_panel.pack()
    print("panel login cargado")

    return login_panel