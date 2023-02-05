import pygame, math, random

class Boid:
    def __init__(self, initialPos, size, color, screen):
        self.position = initialPos
        self.angle = 0
        self.size = size
        self.color = color
        self.screen = screen
        self.scrnDim = [screen.get_width(), screen.get_height()]
        self.bodyPoints = [
							[8*math.cos((math.pi/180)*(self.angle-175))+self.position[0], self.scrnDim[1]-(8*math.sin((math.pi/180)*(self.angle-175))+self.position[1])],
							[8*math.cos((math.pi/180)*(self.angle-185))+self.position[0], self.scrnDim[1]-(8*math.sin((math.pi/180)*(self.angle-185))+self.position[1])],
							[3*math.cos((math.pi/180)*(self.angle+70))+self.position[0], self.scrnDim[1]-(3*math.sin((math.pi/180)*(self.angle+70))+self.position[1])],
							[self.position[0], self.scrnDim[1]-self.position[1]],
							[3*math.cos((math.pi/180)*(self.angle-70))+self.position[0], self.scrnDim[1]-(3*math.sin((math.pi/180)*(self.angle-70))+self.position[1])]
						  ]
    
    def draw(self):
        self.bodyPoints = [
							[8*math.cos((math.pi/180)*(self.angle-175))+self.position[0], self.scrnDim[1]-(8*math.sin((math.pi/180)*(self.angle-175))+self.position[1])],
							[8*math.cos((math.pi/180)*(self.angle-185))+self.position[0], self.scrnDim[1]-(8*math.sin((math.pi/180)*(self.angle-185))+self.position[1])],
							[3*math.cos((math.pi/180)*(self.angle+70))+self.position[0], self.scrnDim[1]-(3*math.sin((math.pi/180)*(self.angle+70))+self.position[1])],
							[self.position[0], self.scrnDim[1]-self.position[1]],
							[3*math.cos((math.pi/180)*(self.angle-70))+self.position[0], self.scrnDim[1]-(3*math.sin((math.pi/180)*(self.angle-70))+self.position[1])]
						  ]
        pygame.draw.polygon(self.screen, self.color, self.bodyPoints)
