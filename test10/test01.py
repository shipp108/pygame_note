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

sprite_pos = Vector2(200, 150)
sprite_speed = 300.

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    key_directory = Vector2(0, 0)
    if pressed_keys[K_LEFT]:
        key_directory.x = -1
    elif pressed_keys[K_RIGHT]:
        key_directory.x = +1
    elif pressed_keys[K_UP]:
        key_directory.y = -1
    elif pressed_keys[K_DOWN]:
        key_directory.y = +1

    key_directory.normalize()

    screen.blit(background, (0, 0))
    screen.blit(sprite, sprite_pos)

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed / 1000.0

    sprite_pos += key_directory * sprite_speed * time_passed_seconds

    pygame.display.update()
