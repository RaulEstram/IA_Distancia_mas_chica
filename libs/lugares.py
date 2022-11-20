from libs.node import Node
from libs.distances import getDistance
from libs.way import Way


class CatalogoLugares:
    lugares = [
        Node("zocalo cdmx", 19.4326018, -99.1332049),
        Node("Fes Aragon", 19.4757307, -99.0446951),
        Node("Ciudad Universitaria", 19.3329456, -99.1851108),
        Node("Aeropuerto ciudad de mexico", 19.4360762, -99.0719083),
        Node("Estacion Metro Cuatro Caminos", 19.459592, -99.215899),
        Node("Forum Buenavista", 19.445844650, -99.150436400),
        Node("Six flags", 19.2953821, -99.2097713702751),
    ]

    @classmethod
    def getListOfWays(cls):
        for main_city in cls.lugares:
            for city in cls.lugares:
                if main_city != city:
                    main_city.caminos.append(Way(city, getDistance(main_city, city)))


CatalogoLugares.getListOfWays()
