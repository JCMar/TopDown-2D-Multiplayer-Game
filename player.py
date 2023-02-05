import pygame, math, random

class Player:
    def __init__(self, initialPos, size, color, screen):
        self.position = initialPos
        self.velocity = [2, 2]
        self.angle = 0
        self.size = size
        self.color = color
        self.screen = screen
        self.scrnDim = [screen.get_width(), screen.get_height()]
    
    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.position[0], self.scrnDim[1]-self.position[1]], 5)