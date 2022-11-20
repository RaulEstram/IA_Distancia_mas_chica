from numpy import round


class Ruta:

    def __init__(self):
        self.nodos = []
        self.totalDistancia = 0

    def __str__(self):
        ruta = ""
        for nodo in self.nodos:
            ruta += nodo.ciudad + " - "
        ruta += f"Distancia recorrida: {round(self.totalDistancia, 2)} Km."
        return ruta
