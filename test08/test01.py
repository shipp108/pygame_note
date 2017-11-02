#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
frame_rate = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load("sushiplate.jpg").convert()
sprite = pygame.image.load("fugu.png").convert_alpha()

x = 0

while True:
    frame_rate.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    x += 10

    if x > 640:
        x = 0;

    pygame.display.update()
