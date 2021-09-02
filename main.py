# Imports the pygame module
import pygame
from pygame.constants import *
from pygame.time import Clock

# Created imports
from mechanics import mechs
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from eventhandler import EventHandler

# Other imports
from os import path
from json import load

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Isaiah's Journey")

clock = Clock()

eventhandler = EventHandler()

# Set home screen
mechs.setup_home_screen()

# CustomEvents
DIALOGUE = USEREVENT + 1
dialogue_event = pygame.event.Event(DIALOGUE, message="Time to send some dialogues")

# Sprite Groups
all_sprites = pygame.sprite.Group()
cactus_sprites = pygame.sprite.Group()

running = True
game_started = 0
game_state = 0
# Custom 

# Dictionary for holding in game data
data_dict = {}

while running:
    # Setting the screen color
    screen.fill(eventhandler.screen_color)

    # Gotta check for those events
    if pygame.event.get(DIALOGUE):
        pass

    eventhandler.check_for_events()
    screen = mechs.load_screen(screen)

    # Gotta make sure they start the game :D
    if not game_started:
        pygame.display.update()
        game_started = pygame.key.get_pressed()[K_RETURN]

        if game_started:
            mechs.gui.clear()
            eventhandler.screen_color = (255, 255, 255)
        else:
            continue

    if not game_state:
        _, new_rect = mechs.write_to_screen("NEW GAME")
        continue_rect = None
        if path.exists("saves.json"):
            _, continue_rect = mechs.write_to_screen("CONTINUE GAME", height_percent_offset=0.7)

        if pygame.mouse.get_pressed()[0]:
            if new_rect.collidepoint(pygame.mouse.get_pos()):
                game_state = 1
            if continue_rect:
                if continue_rect.collidepoint(pygame.mouse.get_pos()):
                    game_state = 2
            if game_state:
                mechs.gui.clear()
                eventhandler.screen_color = (0, 0, 0)
    
    if game_state in [1, 2]:
        if game_state == 1:
            data_dict = mechs.first_time_setup()
            game_state = 3
        else:
            with open("saves.json") as f:
                data_dict = load(f)
            game_state = 4
    
    elif game_state == 3:
        eventhandler.screen_color = (194, 178, 128)
        mechs.write_dialogue("Welcome Hero. It would seem as though you are finally awakening.", pygame.display, screen)
        mechs.write_dialogue("More meaningful text to come here before game begins I guess", pygame.display, screen)
        game_state = 5

    # if game_state == 5:
        # eventhandler.screen_color = (194, 178, 128)

    # Load in sprites
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    clock.tick(30)
