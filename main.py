# Imports the pygame module
from json.decoder import JSONDecodeError
import pygame
from pygame.constants import *
from pygame.time import Clock

# Created imports
from mechanics import mechs
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, gamestate
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

# Sprite Groups
all_sprites = pygame.sprite.Group()
cactus_sprites = pygame.sprite.Group()

running = True
game_started = 0

data_dict = {"WORLD_POS": 0, "PLAYER": {}, "STATES": [], "SPEECH": []}

runtime = 0
while running:
    # Setting the screen color
    screen.fill(eventhandler.screen_color)

    # Gotta check for those events

    eventhandler.check_for_events()
    screen = mechs.load_screen(screen)
    data_dict['DISPLAY'] = pygame.display
    data_dict['SCREEN'] = screen

    # Gotta make sure they start the game :D
    if not game_started:
        pygame.display.update()
        game_started = pygame.key.get_pressed()[K_RETURN]

        if game_started:
            mechs.gui.clear()
            eventhandler.change_bg((255, 255, 255))
        else:
            continue

    if not eventhandler.game_state:
        _, new_rect = mechs.write_to_screen("NEW GAME")
        continue_rect = None
        if path.exists("saves.json"):
            _, continue_rect = mechs.write_to_screen("CONTINUE GAME", height_percent_offset=0.7)

        if pygame.mouse.get_pressed()[0]:
            if new_rect.collidepoint(pygame.mouse.get_pos()):
                eventhandler.game_state = gamestate.STARTED
                
            if continue_rect:
                if continue_rect.collidepoint(pygame.mouse.get_pos()):
                    with open("saves.json") as f:
                        try:
                            data_dict = load(f)
                        except JSONDecodeError:
                            data_dict = {}
                            mechs.write_speech("Save file was corrupted. Fix it, and relaunch or continue on new file", pygame.display, screen)
                        eventhandler.game_state = gamestate.STARTED

            if eventhandler.game_state:
                mechs.gui.clear()
                eventhandler.change_bg((194, 178, 128))
                data_dict["STATES"].append(gamestate.SPEECH)
                data_dict["SPEECH"] = ["Welcome Hero. It would seem as though you are finally awakening.", "More meaningful text to come here before game begins I guess"]
                data_dict["MECHS"] = mechs

        pygame.display.flip()
        continue

    eventhandler.handle_current_state(data_dict)

    # Load in sprites
    for sprite in all_sprites:
        screen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()
    runtime += clock.tick(30)
