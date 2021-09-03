import pygame.sprite as ps
from pygame.image import load
from pygame.transform import scale
from pygame.locals import *
from pygame.event import post, Event
from eventhandler import TERRAINCHANGE
from random import randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(ps.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = scale(load("./Assets/sprites/iseh2.png").convert(), (50, 50))
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(center=(int(SCREEN_WIDTH // 2), int(SCREEN_HEIGHT // 2)))

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
            self.rect.right = SCREEN_WIDTH - 30
            post(Event(TERRAINCHANGE, {}))

        if self.rect.right > SCREEN_WIDTH:
            self.rect.left = 30
            post(Event(TERRAINCHANGE, {}))

        if self.rect.top <= 0:
            self.rect.bottom = SCREEN_HEIGHT - 30
            post(Event(TERRAINCHANGE, {}))

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.top = 30
            post(Event(TERRAINCHANGE, {}))


class NPC(ps.Sprite):
    def __init__(self, spriteimg:str, scaling:tuple, position:tuple, speech=[]):
        super(NPC, self).__init__()
        self.id = id(self)
        self.surf = scale(load(spriteimg).convert(), scaling)
        self.rect = self.surf.get_rect(center=position)
        self.speech = speech

class Vanity(ps.Sprite):
    def __init__(self, spriteimg:str, scaling:tuple):
        super(Vanity, self).__init__()
        self.surf = scale(load(spriteimg).convert(), scaling)
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(center=self.get_position())

    def get_position(self):
        width = randint(20, SCREEN_WIDTH - 20)
        height = randint(20, SCREEN_HEIGHT - 20)
        return (width, height)
