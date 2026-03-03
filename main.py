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


class Doodler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('lik-right.png')
        self.turned_right = True
        self.horizontal_velocity = 10
        self.vertical_velocity = 0
        self.gravity = 0.1
        self.jump_force = 4.5
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.horizontal_velocity
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.horizontal_velocity
        self.keep_within_screen()
        self.vertical_velocity += self.gravity
        self.rect.y += self.vertical_velocity

    def keep_within_screen(self):
        if self.rect.x + self.rect.width <= 0:
            self.rect.x = WIDTH
        elif self.rect.x >= WIDTH:
            self.rect.x = 0 - self.rect.width
    
    def jump(self):
        self.vertical_velocity = -self.jump_force


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('platform-green.png')
        self.pos = x, y
    
    def update(self):
        self.rect.topleft = self.pos


bg_image, bg_rect = load_image('bck.png')

platforms = pygame.sprite.Group()
platforms.add(Platform(0, 0))
platform_height = platforms.sprites()[0].rect.height
gap = 35
for x in range(int(HEIGHT / (platform_height + gap))):
    platforms.add(Platform(0, x * gap))

doodler = pygame.sprite.GroupSingle(Doodler())

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and doodler.sprite.turned_right:
                doodler.sprite.turned_right = False
            if event.key == pygame.K_RIGHT and not doodler.sprite.turned_right:
                doodler.sprite.turned_right = True
            if event.key == pygame.K_SPACE:
                doodler.sprite.jump()
    
    platforms.update()
    doodler.update()
    
    screen.blit(bg_image, (0, 0))
    platforms.draw(screen)
    doodler.draw(screen)

    pygame.display.flip()
