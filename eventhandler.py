import pygame
from pygame.locals import *
from pygame import event

class EventHandler:
    def __init__(self):
        pass

    def check_for_events(self):
        for task in event.get():
            if task == QUIT:
                raise SystemExit()
            if task.type == KEYDOWN:
                self.handle_key_press(task.key)
    
    def handle_key_press(self, key):
        if key == K_ESCAPE:
            raise SystemExit()


eventhandler = EventHandler()