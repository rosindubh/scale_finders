# simple program that moves a car down the screen
# phil welsby - 19 february 2017

import pygame
import sys
import time


screen = pygame.display.set_mode((800, 600))

post = pygame.image.load('post.png').convert()
car = pygame.image.load('car.png').convert()

for i in range(500):
    screen.fill((50,50,50))
    screen.blit(car, (50, i))
    screen.blit(post, (70, 550))
    pygame.display.flip()
    time.sleep(.00225)
screen.fill((50,50,50))
crash = pygame.image.load('crash.png')
screen.blit(crash, (50, i))
pygame.display.flip()

raw_input()
