import sys

import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 60

size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Amazing Doodle Jump")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(FPS)