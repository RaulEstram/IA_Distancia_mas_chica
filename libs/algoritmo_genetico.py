"""
para el algoritmo de este algoritmo utilizamos la metaheurísticas.
Es un método heurístico para resolver un tipo de problema computacional general, usando los parámetros dados por el
usuario sobre unos procedimientos genéricos y abstractos de una manera que se espera eficiente
"""

from libs.node import Node
from libs.ruta import Ruta
from libs.distances import getDistance
import random


class Algorithm:

    def __init__(self, graph: list, n: int, origen: Node):
        self.graph = graph  # el grafo de los lugares a visitar
        self.n = n  # este sera para la aleatoriedad del metodo
        self.origin = origen  # nodo donde se empieza
        self.rutas = []  # las soluciones

    def getRutas(self):
        rutas = ""
        for ruta in self.rutas:
            for node in ruta.nodos:
                rutas += node.ciudad + ", "
            rutas += f"{ruta.totalDistancia}\n"
        return rutas

    # este metodo lo que va hacer es obtener las soluciones
    def run(self):
        # reseteamos las rutas
        self.rutas = []
        # repetimos la cantidad de rutas que queremos, ya que vamos a
        # generar rutas aleatorias para posteriormente elegir la mejor
        for i in range(self.n):
            self.rutas.append(Algorithm.generateRoute(self))
            pass
        # TODO: agregar funcionalidad para orgener la lista para que el primer elemento sea el de menor distancia
        self.rutas.sort(key=lambda x: x.totalDistancia)

    # metodo para generar una ruta
    def generateRoute(self) -> Ruta:
        solucion = Ruta()
        solucion.nodos.append(self.origin)
        nodo_actual = self.origin
        for i in range(len(self.graph) - 1):
            next_node = self.origin
            while next_node in solucion.nodos:
                next_node = random.choice(self.graph)

            solucion.nodos.append(next_node)
            solucion.totalDistancia += getDistance(nodo_actual, next_node)
            nodo_actual = next_node
        solucion.nodos.append(self.origin)
        solucion.totalDistancia += getDistance(nodo_actual, self.origin)
        return solucion
