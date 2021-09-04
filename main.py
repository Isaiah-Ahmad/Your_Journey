# Imports the pygame module
from json.decoder import JSONDecodeError
import pygame
from pygame.constants import *
from pygame.time import Clock
from pygame.event import post, Event

# Created imports
from mechanics import mechs
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, gamestate
from eventhandler import eventhandler, TERRAINCHANGE
from sprites import Player
from terrain import terrain

# Other imports
from os import path
from json import load

pygame.init()
pygame.display.set_caption("Isaiah's Journey")

clock = Clock()

# Sprite Groups
running = True
game_started = 0
was_paused = False

data_dict = {
    "WORLD_POS": 0, 
    "PLAYER": {}, 
    "STATES": [], 
    "SPEECH": [],
    "screen": pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)),
    "display": pygame.display
    }

# Set home screen
mechs.setup_home_screen()

sprite_groups = {"ALLSPRITES": pygame.sprite.Group(), "NPCSPRITES": pygame.sprite.Group(), "DECORSPRITES": pygame.sprite.Group()}
data_dict["SG"] = sprite_groups

runtime = 0
while running:

    # Setting the screen color
    data_dict['screen'].fill(eventhandler.screen_color)

    # Gotta check for those events

    mechs.load_screen(data_dict)
    eventhandler.check_for_events(data_dict)

    # Gotta make sure they start the game :D
    if not game_started:
        data_dict['display'].update()
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
            eventhandler.change_bg((0, 0, 0))
            eventhandler.check_for_events(data_dict)
            if new_rect.collidepoint(pygame.mouse.get_pos()):
                eventhandler.game_state = gamestate.STARTED
                
            if continue_rect:
                if continue_rect.collidepoint(pygame.mouse.get_pos()):
                    with open("saves.json") as f:
                        try:
                            data_dict = data_dict.update(load(f))
                        except JSONDecodeError:
                            mechs.write_speech("Save file was corrupted. Fix it, and relaunch or continue on new file", data_dict)
                        eventhandler.game_state = gamestate.STARTED

            if eventhandler.game_state:
                mechs.gui.clear()
                data_dict["STATES"].append(gamestate.SPEECH)
                data_dict["SPEECH"] = ["Welcome Hero. It would seem as though you are finally awakening.", "Move around with the Arrow Keys"]
                data_dict["MECHS"] = mechs
                player = Player()
                data_dict["PLAYERSPRITE"] = player 
                data_dict["SG"]['ALLSPRITES'].add(player)
                post(Event(TERRAINCHANGE, {}))
                eventhandler.game_state = gamestate.FREEPLAY

        pygame.display.flip()
        continue

    eventhandler.handle_current_state(data_dict)
    if eventhandler.game_state == gamestate.LOADTERRAIN:
        mechs.handle_new_terrain(terrain.generate_terrain(), data_dict)
        eventhandler.game_state = gamestate.FREEPLAY

    mechs.blit_sprites(data_dict)

    if eventhandler.game_state == gamestate.PAUSED:
        save_rect, exit_rect = mechs.setup_pause_screen()
        mechs.load_screen(data_dict)

        if pygame.mouse.get_pressed()[0]:
            if save_rect.collidepoint(pygame.mouse.get_pos()):
                mechs.save(data_dict)
                data_dict["STATES"].append(gamestate.SPEECH)
                data_dict["SPEECH"] = ["Saved"]
            if exit_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                print("Thanks for playin'")
                break

        was_paused = True 
    if was_paused:
        mechs.gui.clear()
        was_paused = False

    if eventhandler.game_state == gamestate.FREEPLAY:
        player.update(pygame.key.get_pressed())

    pygame.display.flip()
    runtime += clock.tick(30)