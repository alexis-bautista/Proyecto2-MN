from sol import sol
from panel import panel
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from datetime import datetime, timedelta


class simulacion:
    @staticmethod
    def plotSolarPath(
        fecha_str, hora_str, duracion, latitude=-0.2105367, longitude=-78.491614
    ):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        sun_positions = []
        panel_positions = []

        def update(frame):
            ax.clear()
            current_time = datetime.strptime(
                f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M"
            ) + timedelta(minutes=frame * 30)
            current_time_str = current_time.strftime("%H:%M")
            az, el = sol.getSolarPosition(
                fecha_str, current_time_str, latitude, longitude
            )

            # Convertir azimuth y altitud a coordenadas cartesianas para graficar
            r = np.cos(np.radians(el))
            x = r * np.sin(np.radians(az))
            y = r * np.cos(np.radians(az))
            z = np.sin(np.radians(el))

            sun_positions.append((x, y, z))

            # Graficar la posición del sol
            ax.scatter(x, y, z, color="yellow", s=600, label="Sol")

            # Graficar una línea que representa los rayos del sol
            ax.plot([0, x], [0, y], [0, z], color="orange", linestyle="--")

            # Graficar el panel solar
            panel_length = 0.50  # Longitud del panel
            panel_width = 0.25  # Ancho del panel

            pitch, roll = panel.calcular_posicion(
                fecha_str, current_time_str, latitude, longitude
            )
            # Crear una matriz de rotación para el pitch y roll
            pitch_matrix = np.array(
                [
                    [1, 0, 0],
                    [0, np.cos(np.radians(pitch)), -np.sin(np.radians(pitch))],
                    [0, np.sin(np.radians(pitch)), np.cos(np.radians(pitch))],
                ]
            )

            roll_matrix = np.array(
                [
                    [np.cos(roll), 0, np.sin(roll)],
                    [0, 1, 0],
                    [-np.sin(roll), 0, np.cos(roll)],
                ]
            )

            rotation_matrix = roll_matrix @ pitch_matrix

            # Coordenadas del panel en su sistema de referencia local
            panel_x = np.array(
                [
                    -panel_length / 2,
                    panel_length / 2,
                    panel_length / 2,
                    -panel_length / 2,
                ]
            )
            panel_y = np.array(
                [-panel_width / 2, -panel_width / 2, panel_width / 2, panel_width / 2]
            )
            panel_z = np.zeros(4)

            panel_coords = np.vstack((panel_x, panel_y, panel_z))
            panel_coords = rotation_matrix @ panel_coords

            panel_positions.append(panel_coords)

            # Graficar el panel solar
            ax.plot_trisurf(
                panel_coords[0],
                panel_coords[1],
                panel_coords[2],
                color="black",
                alpha=0.5,
                label="Panel Solar",
            )

            # Graficar la trayectoria del sol
            if len(sun_positions) > 1:
                sun_x, sun_y, sun_z = zip(*sun_positions)
                ax.plot(
                    sun_x,
                    sun_y,
                    sun_z,
                    color="yellow",
                    linestyle="-",
                    label="Trayectoria del Sol",
                )

            # Graficar la trayectoria del panel
            if len(panel_positions) > 1:
                for i in range(len(panel_positions) - 1):
                    ax.plot(
                        panel_positions[i][0],
                        panel_positions[i][1],
                        panel_positions[i][2],
                        color="black",
                        alpha=0.5,
                    )

            # Etiquetas y título
            ax.set_xlabel("Norte")
            ax.set_ylabel("Este")
            ax.set_zlabel("Altitud")
            ax.set_title(
                f"Posición Solar el {fecha_str} a las {current_time_str} en Lat: {latitude}, Long: {longitude}"
            )
            ax.legend()

        ani = animation.FuncAnimation(
            fig, update, frames=range(duracion * 2 + 1), repeat=False
        )
        plt.show()
