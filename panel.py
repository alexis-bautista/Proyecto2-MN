from sol import sol
import numpy as np


class panel:

    def calcular_posicion(
        fecha_str, hora_str, latitude=-0.2105367, longitude=-78.491614
    ):
        """
        Calcula la posición del panel solar (pitch y roll) para una fecha, hora y ubicación específicas.

        Parametros:
        fecha_str (str): Fecha en formato 'dd/mm/yyyy'.
        hora_str (str): Hora en formato 'HH:MM'.
        latitude (float): Latitud de la ubicación. El valor predeterminado es -0.2105367.
        longitude (float): Longitud de la ubicación. El valor predeterminado es -78.491614.

        Retorna:
        tuple: Pitch y roll del panel en grados.
        """
        az, el = sol.getSolarPosition(fecha_str, hora_str, latitude, longitude)
        print(f"Azimutal: {az}, Elevacion: {el}")

        roll = np.arcsin(np.sin(az) * np.cos(el))

        pitch = np.arcsin(-((np.cos(az) * np.cos(el)) / np.cos(roll)))
        pitch_deg = np.degrees(pitch)

        return pitch_deg, roll
