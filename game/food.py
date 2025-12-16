import pygame
import random

class Food:
    def __init__(self, width, height, block):
        self.width = width
        self.height = height
        self.block = block
        self.spawn()

    def spawn(self):
        self.x = random.randrange(0, self.width, self.block)
        self.y = random.randrange(0, self.height, self.block)

    def draw(self, win):
        pygame.draw.rect(
            win,
            (255, 0, 0),
            (self.x, self.y, self.block, self.block)
        )
# hehehehehe