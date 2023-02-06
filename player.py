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
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.position[0] -= self.velocity[0]
        elif keys[pygame.K_d]:
            self.position[0] += self.velocity[0]
        
        if keys[pygame.K_w]:
            self.position[1] += self.velocity[1]
        elif keys[pygame.K_s]:
            self.position[1] -= self.velocity[1]

    def draw(self):
        self.move()
        pygame.draw.circle(self.screen, self.color, [self.position[0], self.scrnDim[1]-self.position[1]], 5)