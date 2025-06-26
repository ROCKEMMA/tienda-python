import tkinter as tk

class PanelHijo(tk.Frame):
    def __init__(self, padre, callback_actualizar, **kwargs):
        super().__init__(padre, **kwargs)
        self.callback_actualizar = callback_actualizar

        boton = tk.Button(self, text="Actualizar Padre", command=self.actualizar_padre)
        boton.pack()

    def actualizar_padre(self):
        self.callback_actualizar("¡Texto actualizado desde el hijo!")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Padre")

        self.etiqueta = tk.Label(self, text="Texto original")
        self.etiqueta.pack()

        hijo = PanelHijo(self, self.actualizar_texto)
        hijo.pack()

    def actualizar_texto(self, nuevo_texto):
        self.etiqueta.config(text=nuevo_texto)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
