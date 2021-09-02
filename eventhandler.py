from pygame.locals import *
from pygame import event, QUIT
from constants import gamestate
from terrain import Terrain

# CustomEvents
BGCHANGE = USEREVENT + 1
GAMESTATECHANGE = USEREVENT + 2
TERRAINCHANGE = USEREVENT + 3

class EventHandler:
    def __init__(self):
        # self.screen_color = (194,178,128)
        self.screen_color = (51, 51, 51)
        self.game_state = 0
        self.terrain = Terrain()

    def check_for_events(self):
        for task in event.get():
            if task.type == QUIT:
                raise SystemExit()
            if task.type == KEYDOWN:
                self.handle_key_press(task.key)       
            if task.type == BGCHANGE:
                self.screen_color = task.color 
            if task.type == TERRAINCHANGE:
                self.handle_changing_terrain()

    def change_bg(self, color):
        ev = event.Event(BGCHANGE, {"color": color})
        event.post(ev)

    def change_game_state(self, data_dict):
        ev = event.Event(GAMESTATECHANGE, data_dict)
        event.post(ev)
    
    def handle_key_press(self, key):
        if key == K_ESCAPE:
            raise SystemExit()

    def handle_state_change(self, state, data_dict):
        if state == gamestate.SPEECH:
            for speech in data_dict["SPEECH"]:
                data_dict["MECHS"].write_speech(speech, data_dict["DISPLAY"], data_dict["SCREEN"])

            data_dict["SPEECH"].clear()

    def handle_current_state(self, data_dict):
        if not data_dict['STATES']: self.handle_state_change(self.game_state, data_dict)
        [self.handle_state_change(state, data_dict) for state in data_dict['STATES']]

        data_dict["STATES"].clear()

    def handle_changing_terrain(self):
        terrain = self.terrain.load_terrain()
        self.screen_color = terrain['COLOR']

