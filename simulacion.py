from sol import sol
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class simulacion:
    @staticmethod
    def plotSolarPath(fecha_str, hora_str, latitude=-0.2105367, longitude=-78.491614):
        az, el = sol.getSolarPosition(fecha_str, hora_str, latitude, longitude)

        # Convertir azimuth y altitud a coordenadas cartesianas para graficar
        r = np.cos(np.radians(el))
        x = r * np.sin(np.radians(az))
        y = r * np.cos(np.radians(az))
        z = np.sin(np.radians(el))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # Graficar la posición del sol
        ax.scatter(x, y, z, color="r", s=200, label="Sol")

        # Graficar una línea que representa los rayos del sol
        ax.plot([0, x], [0, y], [0, z], color="orange", linestyle="--")

        # Etiquetas y título
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Altitud")
        ax.set_title(
            f"Posición Solar el {fecha_str} a las {hora_str} en Lat: {latitude}, Long: {longitude}"
        )
        ax.legend()

        plt.show()
