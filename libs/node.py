class Node:
    def __init__(self, ciudad: str, lat: float, long: float):
        self.ciudad = ciudad
        self.latitud = lat
        self.longitud = long
        self.caminos = []

    def __str__(self):
        return f"{self.ciudad} ({self.latitud}, {self.longitud})"
