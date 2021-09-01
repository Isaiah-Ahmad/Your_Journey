from pygame.locals import *
from pygame import event, QUIT

class EventHandler:
    def __init__(self, screen):
        self.screen = screen
        self.screen_color = (194,178,128)

    def check_for_events(self):
        for task in event.get():
            if task.type == QUIT:
                raise SystemExit()
            if task.type == KEYDOWN:
                self.handle_key_press(task.key)
        
        self.screen.fill(self.screen_color)
        
    
    def handle_key_press(self, key):
        if key == K_ESCAPE:
            raise SystemExit()

