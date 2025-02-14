import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
from PIL import Image, ImageTk

# from sol import sol
from panel import panel
from simulacion import simulacion

colores = {
    "fondo": "#e6f7ff",
    "principal": "#003366",
    "texto": "#003366",
    "boton_texto": "white",
    "activo": "#00509e",
}


class SeguidorSolarApp:
    def __init__(self, root):
        """
        Inicializa la aplicación de la GUI del seguidor solar.

        Parametros:
        root (tk.Tk): La ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("SEGUIDOR SOLAR")
        self.root.configure(bg=colores["fondo"])
        self.root.geometry("800x600")

        self.crear_estilos()
        self.crear_widgets_principal()

    def crear_estilos(self):
        """
        Crea y configura los estilos para los widgets de la aplicación.
        """
        estilo = ttk.Style()
        estilo.theme_use("default")
        estilo.configure(
            "TFrame",
            background=colores["fondo"],
        )
        estilo.configure(
            "TLabel",
            background=colores["fondo"],
            foreground=colores["texto"],
            font=("Arial", 12),
        )
        estilo.configure(
            "TButton",
            background=colores["principal"],
            foreground=colores["boton_texto"],
            font=("Arial", 10, "bold"),
            padding=6,
        )
        estilo.map("TButton", background=[("active", colores["activo"])])

        estilo.configure(
            "Custom.TLabel", background=colores["fondo"], foreground=colores["texto"]
        )
        estilo.configure(
            "Custom.TButton",
            background=colores["principal"],
            foreground=colores["boton_texto"],
        )

    def crear_widgets_principal(self):
        """
        Crea y coloca los widgets en la ventana principal de la aplicación.
        """
        frame = ttk.Frame(self.root, padding=20, style="TFrame")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(
            frame,
            text="SEGUIDOR SOLAR - Proyecto de Métodos Númericos",
            font=("Arial", 16, "bold"),
            style="Custom.TLabel",
        ).grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        # Cargar y mostrar la imagen
        try:
            img = Image.open("ADJUNTOS/PortadaSeguidor.jpeg")
            img = img.resize((200, 200))
            img_tk = ImageTk.PhotoImage(img)

            img_label = tk.Label(frame, image=img_tk, bg=colores["fondo"])
            img_label.image = (
                img_tk  # Mantener referencia para evitar recolección de basura
            )
            img_label.grid(row=1, column=0, columnspan=2, pady=10)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

        ttk.Label(frame, text="Fecha (DD/MM/AAAA):", style="Custom.TLabel").grid(
            row=2, column=0, sticky="e", pady=5
        )
        self.fecha = DateEntry(frame, font=("Arial", 10), date_pattern="dd/MM/yyyy")
        self.fecha.grid(row=2, column=1, pady=5, padx=10)

        ttk.Label(frame, text="Hora (HH:MM):", style="Custom.TLabel").grid(
            row=3, column=0, sticky="e", pady=5
        )
        self.hora = ttk.Entry(frame, font=("Arial", 10))
        self.hora.grid(row=3, column=1, pady=5, padx=10)

        ttk.Label(frame, text="Duración (horas):", style="Custom.TLabel").grid(
            row=4, column=0, sticky="e", pady=5
        )
        self.duracion = ttk.Spinbox(
            frame, from_=1, to=12, font=("Arial", 10), state="readonly"
        )
        self.duracion.grid(row=4, column=1, pady=5, padx=10)

        ttk.Button(
            frame,
            text="Iniciar Simulación",
            command=self.mostrar_simulacion,
            style="Custom.TButton",
        ).grid(row=5, column=0, columnspan=2, pady=20)

        # Integrantes
        integrantes = "By: Alexis Bautista, David Egas, Aubertin Ochoa, Erick Romero"
        label_integrante = ttk.Label(
            self.root, text=f"{integrantes}", style="Custom.TLabel"
        )
        label_integrante.place(x=790, y=590, anchor="se")

    def mostrar_simulacion(self):
        """
        Obtiene los datos ingresados por el usuario y muestra la simulación de la trayectoria solar.
        """
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
        """
        Valida si la hora ingresada está dentro del rango visible del sol.

        Parametros:
        hora (datetime.time): La hora a validar.

        Retorna:
        bool: True si la hora está entre las 6:00 y las 18:00, False en caso contrario.
        """
        return 6 <= hora.hour <= 18

    def calcular_duracion_real(self, fecha, hora, duracion):
        """
        Calcula la duración real de la simulación basada en la visibilidad del sol.

        Parametros:
        fecha (datetime.date): La fecha de la simulación.
        hora (datetime.time): La hora de inicio de la simulación.
        duracion (int): La duración solicitada de la simulación en horas.

        Retorna:
        int: La duración real de la simulación en horas.
        """
        hora_fin = datetime.combine(fecha, hora) + timedelta(hours=duracion)
        if hora_fin.time().hour > 18:
            return 18 - hora.hour
        return duracion


if __name__ == "__main__":
    root = tk.Tk()
    app = SeguidorSolarApp(root)
    root.mainloop()
