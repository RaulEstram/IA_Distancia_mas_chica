from numpy import sin, cos, arccos, pi, round
from libs.node import Node


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees


def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians


def getDistance(node1: Node, node2: Node):
    theta = node1.longitud - node2.longitud

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(node1.latitud)) * sin(deg2rad(node2.latitud))) +
            (cos(deg2rad(node1.latitud)) * cos(deg2rad(node2.latitud)) * cos(deg2rad(theta)))
        )
    )

    return round(distance * 1.609344, 2)
