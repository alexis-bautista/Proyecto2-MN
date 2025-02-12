from pysolar.solar import get_altitude, get_azimuth
from datetime import datetime, timedelta
from pytz import timezone


class sol:
    @staticmethod
    def getSolarPosition(
        fecha_str, hora_str, latitude=-0.2105367, longitude=-78.491614
    ):
        """
        Obtiene la posición solar (azimut y altitud) para una fecha, hora y ubicación específicas.

        Parametros:
        fecha_str (str): Fecha en formato 'dd/mm/yyyy'.
        hora_str (str): Hora en formato 'HH:MM'.
        latitude (float): Latitud de la ubicación. El valor predeterminado es -0.2105367.
        longitude (float): Longitud de la ubicación. El valor predeterminado es -78.491614.

        Return:
        tuple: Azimut y altitud del sol en grados.
        """
        date = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M").replace(
            tzinfo=timezone("America/Guayaquil")
        )

        az = get_azimuth(latitude, longitude, date)
        el = get_altitude(latitude, longitude, date)

        return az, el
