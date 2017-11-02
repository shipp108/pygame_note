# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
WIDTH = 640
HEIGHT = 480
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 40)

text_surface = font.render(u"hello", True, (0, 0, 255))

x = 0
y = (HEIGHT - text_surface.get_height()) / 2

try:
    background = pygame.image.load("sushiplate.jpg").convert()
except pygame.error, e:
    print e
    exit()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    x -= 2
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))
    pygame.display.update()
