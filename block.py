import pygame, math

class Block:
	def __init__(self, position, obstacleSize, color, screen):
		self.position = position
		self.obstacleSize = obstacleSize
		self.color = color
		self.screen = screen
		self.screenWidth = screen.get_width()
		self.screenHeight = screen.get_height()
		self.isObstacle = False
		self.tile = pygame.image.load('assests/Block_C_02.png').convert()
		self.tile = pygame.transform.scale(self.tile, self.obstacleSize)

	def draw(self):
		self.screen.blit(self.tile, (self.position[0], self.screenHeight-self.position[1]))
