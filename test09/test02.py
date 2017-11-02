#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load("sushiplate.jpg").convert()
sprite = pygame.image.load("fugu.png").convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick(50)
    time_passed_seconds = time_passed / 1000.0

    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2
    vector_to_mouse = Vector2.from_points(position, destination)
    speed = vector_to_mouse.get_magnitude() * 2
    vector_to_mouse.normalize()

    heading = (vector_to_mouse * speed)

    position += heading * time_passed_seconds
    pygame.display.update()
    
