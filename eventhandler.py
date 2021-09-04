from pygame.locals import *
from pygame.event import Event, post, get
from pygame import QUIT
from pygame import mouse
from constants import gamestate

# CustomEvents
BGCHANGE = USEREVENT + 1
GAMESTATECHANGE = USEREVENT + 2
TERRAINCHANGE = USEREVENT + 3

class EventHandler:
    def __init__(self):
        # self.screen_color = (194,178,128)
        self.screen_color = (51, 51, 51)
        self.game_state = 0

    def check_for_events(self, data_dict):
        for task in get():
            if task.type == QUIT:
                raise SystemExit()
            if task.type == KEYDOWN:
                self.handle_key_press(task.key)       
            if task.type == BGCHANGE:
                self.screen_color = task.color 
            if task.type == TERRAINCHANGE:
                self.game_state = gamestate.LOADTERRAIN
            if task.type == MOUSEBUTTONDOWN:
                self.check_for_mouse_collisions(data_dict)
        return data_dict

    def change_bg(self, color):
        ev = Event(BGCHANGE, {"color": color})
        post(ev)

    def change_game_state(self, data_dict):
        ev = Event(GAMESTATECHANGE, data_dict)
        post(ev)
    
    def handle_key_press(self, key):
        if key == K_ESCAPE:
            self.game_state = gamestate.PAUSED if self.game_state == gamestate.FREEPLAY else gamestate.FREEPLAY

    def handle_state_change(self, state, data_dict):
        if state == gamestate.SPEECH:
            for speech in data_dict["SPEECH"]:
                data_dict["MECHS"].write_speech(speech, data_dict)

            data_dict["SPEECH"].clear()

    def handle_current_state(self, data_dict):
        if not data_dict['STATES']: self.handle_state_change(self.game_state, data_dict)
        [self.handle_state_change(state, data_dict) for state in data_dict['STATES']]

        data_dict["STATES"].clear()

    def check_for_mouse_collisions(self, data_dict):
        print("Mouse was pressed")
        for sprite in data_dict["SG"]["ALLSPRITES"]:
            if sprite.rect.collidepoint(mouse.get_pos()):
                if hasattr(sprite, "speech"):
                    if sprite.speech:
                        data_dict['STATES'].append(gamestate.SPEECH)
                        data_dict['SPEECH'] = sprite.speech

eventhandler = EventHandler()