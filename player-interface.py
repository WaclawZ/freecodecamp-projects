from abc import ABC, abstractmethod
from random import choice

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self) -> tuple:
        move = choice(self.moves)
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        self.position = new_position
        self.path.append(new_position)
        return new_position
    
    @abstractmethod
    def level_up(self):
        pass
