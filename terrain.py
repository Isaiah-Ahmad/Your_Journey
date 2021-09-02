from random import choice
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Options for terrain dictionaries:
"""
COLOR: tuple
OPTIONAL:
    NPC: list of dicts
        Dict Contents:
            SRC: path to sprite image (str)
            SCALE: Size of the sprite (tuple)
            POS: Position to place the sprite (tuple)
            OPTIONAL:
                SPEECH: Text for npc to say (list(str))
"""
terrain_types = {
    "SANDY": {"COLOR": (194, 178, 128)},
    "FOREST": {"COLOR": (50, 220, 50), "NPC":{
        "SRC": "./Assets/sprites/soda.png",
        "SCALE": (80, 120),
        "POS": (int(SCREEN_WIDTH * 0.8), int(SCREEN_HEIGHT * 0.4)),
        "SPEECH": ["Why hello there young man...", "Me? Don't worry about who I am", "I'm here to guide you :D"]
    }},
    "MOUNTAIN": {"COLOR": (252, 140, 64)}
}

class Terrain:
    def __init__(self) -> None:
        pass

    def generate_terrain(self):
        return terrain_types[choice(tuple(terrain_types.keys()))]

terrain = Terrain()