import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta

# from sol import sol
from panel import panel
from simulacion import simulacion

colores = {
    "fondo": "#f0f4f8",
    "principal": "#4caf50",
    "secundario": "#c8e6c9",
    "texto": "#212121",
    "boton_texto": "#000000",
}


class SeguidorSolarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SEGUIDOR SOLAR")
        self.root.configure(bg=colores["fondo"])
        self.root.geometry("800x600")

        self.crear_estilos()
        self.crear_widgets_principal()

    def crear_estilos(self):
        estilo = ttk.Style()
        estilo.configure(
            "TFrame",
            background=colores["fondo"],
        )
        estilo.configure(
            "TLabel",
            background=colores["fondo"],
            foreground=colores["texto"],
            font=("Helvetica", 11),
        )
        estilo.configure(
            "TButton",
            background=colores["principal"],
            foreground=colores["boton_texto"],
            font=("Helvetica", 10, "bold"),
            padding=6,
        )
        estilo.map("TButton", background=[("active", "#005f99")])

        # Apply styles to specific widgets
        estilo.configure(
            "Custom.TLabel", background=colores["fondo"], foreground=colores["texto"]
        )
        estilo.configure(
            "Custom.TButton",
            background=colores["principal"],
            foreground=colores["boton_texto"],
        )

    def crear_widgets_principal(self):
        frame = ttk.Frame(self.root, padding=20, style="TFrame")
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(
            frame,
            text="SEGUIDOR SOLAR - Proyecto de Metodos Numericos",
            font=("Helvetica", 16, "bold"),
            style="Custom.TLabel",
        ).grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Label(frame, text="Fecha (DD/MM/AAAA):", style="Custom.TLabel").grid(
            row=1, column=0, sticky="e", pady=5
        )
        self.fecha = DateEntry(frame, font=("Helvetica", 10), date_pattern="dd/MM/yyyy")
        self.fecha.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(frame, text="Hora (HH:MM):", style="Custom.TLabel").grid(
            row=2, column=0, sticky="e", pady=5
        )
        self.hora = ttk.Entry(frame, font=("Helvetica", 10))
        self.hora.grid(row=2, column=1, pady=5, padx=10)

        ttk.Label(frame, text="Duración (horas):", style="Custom.TLabel").grid(
            row=3, column=0, sticky="e", pady=5
        )
        self.duracion = ttk.Spinbox(frame, from_=1, to=24, font=("Helvetica", 10))
        self.duracion.grid(row=3, column=1, pady=5, padx=10)

        ttk.Button(
            frame,
            text="Iniciar Simulación",
            command=self.mostrar_simulacion,
            style="Custom.TButton",
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def mostrar_simulacion(self):
        fecha_str = self.fecha.get()
        hora_str = self.hora.get()
        duracion = self.duracion.get()

        if not fecha_str or not hora_str or not duracion:
            messagebox.showerror("Error", "Ingrese todos los datos requeridos.")
            return

        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            hora = datetime.strptime(hora_str, "%H:%M").time()
            duracion = int(duracion)
        except ValueError:
            messagebox.showerror("Error", "Fecha u hora incorrecta. Intente de nuevo.")
            return

        if not self.validar_hora_sol(hora):
            messagebox.showinfo(
                "Información",
                "El sol no es visible a estas horas. Intente en un rango de 6:00 a 18:00.",
            )
            return

        pitch, roll = panel.calcular_posicion(fecha_str, hora_str)
        print(f"Roll: {roll}, Pitch: {pitch}")

        duracion_real = self.calcular_duracion_real(fecha, hora, duracion)
        if duracion_real < duracion:
            messagebox.showinfo(
                "Información",
                f"La simulación se hará por {duracion_real} horas dado que el sol a las {hora.hour + duracion_real} horas estará oculto.",
            )
            duracion = duracion_real

        simulacion.plotSolarPath(fecha_str, hora_str, duracion)

    def validar_hora_sol(self, hora):
        return 6 <= hora.hour <= 18

    def calcular_duracion_real(self, fecha, hora, duracion):
        hora_fin = datetime.combine(fecha, hora) + timedelta(hours=duracion)
        if hora_fin.time().hour > 18:
            return 18 - hora.hour
        return duracion


if __name__ == "__main__":
    root = tk.Tk()
    app = SeguidorSolarApp(root)
    root.mainloop()
