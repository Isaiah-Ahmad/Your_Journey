# Imports the pygame module
import pygame
from pygame.constants import *
from pygame.time import Clock

# Created imports
from mechanics import mechs
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from eventhandler import EventHandler


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Isaiah's Journey")

clock = Clock()

eventhandler = EventHandler()

# Set home screen
mechs.setup_home_screen()

# Sprite Groups
all_sprites = pygame.sprite.Group()
cactus_sprites = pygame.sprite.Group()

running = True
playing = False
while running:
    # Setting the screen color
    screen.fill(eventhandler.screen_color)
    # Gotta make sure they start the game :D
    if not playing:
        screen = mechs.load_screen(screen)
        eventhandler.check_for_events()
        pygame.display.update()
        continue

    # Gotta check for those events
    eventhandler.check_for_events()

    # Load in sprites
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
