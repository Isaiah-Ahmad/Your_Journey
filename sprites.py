import pygame.sprite as ps
from pygame.image import load
from pygame.transform import scale
from pygame.locals import *
from random import randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(ps.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = scale(load("./Assets/sprites/iseh2.png").convert(), (50, 50))
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed):
        if pressed[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Cactus(ps.Sprite):
    def __init__(self):
        super(Cactus, self).__init__()
        self.surf = scale(load("./Assets/sprites/cactus.png").convert(), (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                randint(30, SCREEN_WIDTH - 100),
                randint(0, SCREEN_HEIGHT - 20)
            ))