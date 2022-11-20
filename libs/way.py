from libs.node import Node


class Way:
    def __init__(self, node: Node, distancia: float):
        self.node = node
        self.distancia = distancia
