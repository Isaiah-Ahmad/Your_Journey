from sprites import Cactus
from random import randint, sample

class Mechanics:
    def __init__(self) -> None:
        pass

    def should_generate(self, chance, max):
        valid = sample(range(max), k=chance)
        value = randint(0, max)
        return value in valid


mechs = Mechanics()