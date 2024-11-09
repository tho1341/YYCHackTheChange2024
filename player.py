import pygame
from sprite import Sprite

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movement_speed = 2

    def update(self):
        
