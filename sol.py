from pysolar.solar import get_altitude, get_azimuth
from datetime import datetime, timedelta
from pytz import timezone


class sol:
    @staticmethod
    def getSolarPosition(
        fecha_str, hora_str, latitude=-0.2105367, longitude=-78.491614
    ):
        date = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M").replace(
            tzinfo=timezone("America/Guayaquil")
        )

        az = get_azimuth(latitude, longitude, date)
        el = get_altitude(latitude, longitude, date)

        return az, el
