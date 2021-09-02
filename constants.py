from pyautogui import size

screen_size = size()

SCREEN_WIDTH, SCREEN_HEIGHT = int(screen_size[0]), int(screen_size[1])

class GameState:
    STARTED = 1
    FREEPLAY = 2
    SPEECH = 3 # Requires Mechs, Display, Screen, Dialogues
    MAKEPLAYER = 10

gamestate = GameState()
