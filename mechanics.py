from eventhandler import BGCHANGE
from json import dump
from random import randint, sample
from pygame.font import Font
from pygame.image import load
from pygame.surface import Surface
from pygame.transform import scale
from pygame.time import delay
from pygame.event import post, Event
from sprites import NPC
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

    def setup_pause_screen(self):
        surface = Surface((int(SCREEN_WIDTH * 0.4), int(SCREEN_HEIGHT * 0.7)))
        surface.fill((255, 255, 255))
        surface_rect = surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pause = self.set_render_text("Paused?", width_percent_offset=0.5, height_percent_offset=0.3, colors=(180, 180, 180))
        resume = self.set_render_text("Press P to resume or ESC to quit", 20, 0.5, 0.4, colors=(40, 40, 40))
        save = self.set_render_text("Save", 25, 0.4, 0.6)

        
        self.gui.extend([(surface, surface_rect), pause, resume, save])
        return save[1]

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

    def save(self, data_dict):
        to_save = {}

        with open("saves.json", "w") as f:
            dump(to_save, f, indent=4)

    def load_screen(self, screen):
        [screen.blit(gui[0], gui[1]) for gui in self.gui]
        return screen

    def blit_sprites(self, all_sprites, screen):
        for sprite in all_sprites:
            screen.blit(sprite.surf, sprite.rect)

    def handle_new_terrain(self, terrain:dict, data_dict: dict, npc_sprites, all_sprites):
        color = terrain["COLOR"]
        if terrain.get('NPC', None):
            new_npc = NPC(terrain["NPC"]["SRC"], terrain['NPC']['SCALE'], terrain['NPC']['POS'], terrain['NPC'].get("SPEECH", []))
            data_dict["NPCS"].append(new_npc)
            npc_sprites.add(new_npc)
            all_sprites.add(new_npc)

        post(Event(BGCHANGE, {"color": color}))

        return npc_sprites, all_sprites

    def should_generate(self, chance, max):
        valid = sample(range(max), k=chance)
        value = randint(0, max)
        return value in valid

mechs = Mechanics()