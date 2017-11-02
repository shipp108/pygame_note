#!/usr/bin/env python
import gameobjects.vector3 import *

def parallel_project(vector3):
    return (vector3.x, vector3.y)

def perspective_project(vector3, d):
    x, y, z = vector3
    return (x * d / z, -y * d / z)

from math import tan

def calculate_viewing_distance(fov, screen_width):
    d = (screen_width / 2.0) / tan(fov / 2.0)
    return d
