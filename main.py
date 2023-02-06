import pygame, random

pygame.init()
from boid import *
from block import *
from player import *

screen = pygame.display.set_mode((1100, 600))
clock = pygame.time.Clock()

player = Player([550,300], 10, (255,255,0), screen)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    screen.fill((0, 0, 0))
    player.draw()
    pygame.display.update()
    clock.tick(120)
