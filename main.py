# Imports the pygame module
import pygame
from pygame.constants import *
from pygame.time import Clock

# Created imports
from sprites import Player
from mechanics import mechs
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from eventhandler import EventHandler


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = Clock()

eventhandler = EventHandler(screen)

mp = Player()

# Sprite Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(mp)

cactus_sprites = pygame.sprite.Group()

running = True
while running:
    # Gotta check for those events
    eventhandler.check_for_events()
            
    mp.update(pygame.key.get_pressed())

    cactus_sprites, all_sprites = mechs.generate_cacti(cactus_sprites, all_sprites)

    # Load in sprites
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    clock.tick(30)
