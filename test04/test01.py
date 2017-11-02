#!/usr/bin/env python
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

font_ = pygame.font.SysFont("arial", 16)
surface_ = font_.render("Hello world", True, (0, 0, 0), (255, 255, 255))

pygame.image.save(surface_, "save.png")
