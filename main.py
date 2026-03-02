import os
import sys

import pygame

pygame.init()

WIDTH = 320
HEIGHT = 512
FPS = 60

size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Amazing Doodle Jump")
clock = pygame.time.Clock()

current_dir = os.path.split(os.path.abspath(__file__))[0]
images_dir = os.path.join(current_dir, "images")

def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(images_dir, name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()

    image = pygame.transform.scale_by(image, scale)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    
    return image, image.get_rect()


bg_image, bg_rect = load_image('bck.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(bg_image, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)
