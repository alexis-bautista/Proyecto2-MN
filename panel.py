from sol import sol
import numpy as np


class panel:

    def calcular_posicion(
        fecha_str, hora_str, latitude=-0.2105367, longitude=-78.491614
    ):
        az, el = sol.getSolarPosition(fecha_str, hora_str, latitude, longitude)
        print(f"Azimutal: {az}, Elevacion: {el}")

        roll = np.arcsin(np.sin(az) * np.cos(el))

        pitch = np.arcsin(-((np.cos(az) * np.cos(el)) / np.cos(roll)))
        pitch_deg = np.degrees(pitch)

        return pitch_deg, roll
