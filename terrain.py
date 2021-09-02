from random import choice
terrain_types = {
    "SANDY": {"COLOR": (194, 178, 128)},
    "FOREST": {"COLOR": (50, 220, 50)},
    "MOUNTAIN": {"COLOR": (252, 140, 64)}
}

class Terrain:
    def __init__(self) -> None:
        pass

    def load_terrain(self):
        return terrain_types[choice(tuple(terrain_types.keys()))]