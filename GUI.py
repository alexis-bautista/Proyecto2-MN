import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from sol import sol
from simulacion import simulacion

colores = {
    "fondo": "#e6f7ff",
    "principal": "#003366",  # Negro
    "secundario": "#CCCCCC",  # Gris claro
    "texto": "#333333",  # Gris oscuro
}


class SeguidorSolarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seguidor Solar")
        self.root.configure(bg=colores["fondo"])

        self.crear_widgets_principal()

    def crear_widgets_principal(self):
        # Frame contenedor
        frame = ttk.Frame(self.root, padding=20)
        frame.grid(row=0, column=0, sticky="nsew")

        # Widgets para fecha y hora
        ttk.Label(
            frame,
            text="Fecha (DD/MM/AAAA):",
            background=colores["fondo"],
            foreground=colores["texto"],
        ).grid(row=0, column=0, sticky="w")
        self.fecha = ttk.Entry(frame)
        self.fecha.grid(row=0, column=1, pady=5)

        ttk.Label(
            frame,
            text="Hora (HH:MM):",
            background=colores["fondo"],
            foreground=colores["texto"],
        ).grid(row=1, column=0, sticky="w")
        self.hora = ttk.Entry(frame)
        self.hora.grid(row=1, column=1, pady=5)

        ttk.Label(
            frame,
            text="Duración (horas):",
            background=colores["fondo"],
            foreground=colores["texto"],
        ).grid(row=2, column=0, sticky="w")
        self.duracion = ttk.Spinbox(frame, from_=1, to=24)
        self.duracion.grid(row=2, column=1, pady=5)

        # Botón de ingreso
        ttk.Button(
            frame,
            text="Iniciar Simulación",
            command=self.mostrar_simulacion,
            style="Principal.TButton",
        ).grid(row=3, column=0, columnspan=2, pady=20)

        # Estilos
        estilo = ttk.Style()
        estilo.configure(
            "Principal.TButton",
            foreground=colores["fondo"],
            background=colores["principal"],
            font=("Helvetica", 10, "bold"),
        )

    def mostrar_simulacion(self):
        # Obtener datos de la interfaz
        fecha_str = self.fecha.get()
        hora_str = self.hora.get()
        duracion = int(self.duracion.get())

        # Convertir a datetime
        fecha_hora = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
        fin_simulacion = fecha_hora + timedelta(hours=duracion)

        # Llamar a la lógica de simulación
        az, el = sol.getSolarPosition(fecha_str, hora_str)
        print(f"Azimutal: {az}, Elevacion: {el}")

        simulacion.plotSolarPath(fecha_str, hora_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = SeguidorSolarApp(root)
    root.mainloop()
