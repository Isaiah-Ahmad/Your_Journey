from random import randint, sample
from pygame.font import Font
from pygame.image import load
from pygame.surface import Surface
from pygame.transform import scale
from pygame.time import delay
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

    def write_to_screen(self, text, width_percent_offset=0.5, height_percent_offset=0.5, colors=(150, 150, 150), background=None):
        word_info = self.set_render_text(text, 31, width_percent_offset, height_percent_offset, colors, background)
        self.gui.append(word_info)
        return word_info

    def write_speech(self, text, display, screen):
        display.flip()
        text = self.set_render_text(text, 30, 0.5, 0.8, (200, 200, 200))
        dbox = Surface((int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.3)))
        dbox.fill((100, 100, 100))
        dbox_rect = dbox.get_rect(center=text[1].center)
        screen.blit(dbox, dbox_rect)
        screen.blit(text[0], text[1])
        display.flip()

        delay(4000)    

    def set_render_text(self, text, font_size=31, width_percent_offset=0.5, height_percent_offset=0.5, colors=(150, 150, 150), background=None):
        font = Font("freesansbold.ttf", font_size)
        words = font.render(text, True, colors, background)
        word_rect = words.get_rect(center= (
            int(SCREEN_WIDTH * width_percent_offset),
            int(SCREEN_HEIGHT * height_percent_offset)
        ))

        return (words, word_rect)

    def load_screen(self, screen):
        [screen.blit(gui[0], gui[1]) for gui in self.gui]
        return screen

    def should_generate(self, chance, max):
        valid = sample(range(max), k=chance)
        value = randint(0, max)
        return value in valid

mechs = Mechanics()