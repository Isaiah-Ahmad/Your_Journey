from random import randint, sample
from pygame.font import Font
from pygame.image import load
from pygame.transform import scale
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Mechanics:
    def __init__(self) -> None:
        self.gui = []
        

    def setup_home_screen(self):
        # Title
        title = scale(load("./Assets/images/text.png").convert(), (int(SCREEN_WIDTH * 0.7), int(SCREEN_HEIGHT * 0.7)))
        title.set_colorkey((0, 0, 0))
        title_rect = title.get_rect(center=((SCREEN_WIDTH // 2), int(SCREEN_HEIGHT * 0.2)))

        sword = scale(load("./Assets/images/sword.png").convert(), (int(SCREEN_WIDTH * 0.3), int(SCREEN_HEIGHT * 0.7)))
        sword.set_colorkey((0, 0, 0))
        sword_rect = sword.get_rect(center=((SCREEN_WIDTH // 2), int(SCREEN_HEIGHT * 0.4)))
        
        start_font = Font('freesansbold.ttf', 35)
        start_text = start_font.render("Press the ENTER key to begin", True, (200, 200, 200))
        start_text_rect = start_text.get_rect(center=(int(SCREEN_WIDTH // 2), int(SCREEN_HEIGHT * 0.8)))
        
        self.gui.append((sword, sword_rect))
        self.gui.append((title, title_rect))
        self.gui.append((start_text, start_text_rect))

    def load_screen(self, screen):
        for gui in self.gui:
            screen.blit(gui[0], gui[1])

        return screen

    def should_generate(self, chance, max):
        valid = sample(range(max), k=chance)
        value = randint(0, max)
        return value in valid


mechs = Mechanics()