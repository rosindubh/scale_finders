#  written using jones rapid game development pdf.
# 18 february - phil welsby

import pygame, sys
import math
import time
import random

pygame.init()

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 30
deltat = clock.tick(FRAMES_PER_SECOND)

screen = pygame.display.set_mode((1080, 720))
raw_input()
ball = pygame.image.load('ball.bmp')

for i in range(-40, 1080):
    screen.fill((0, 0, 0))
    screen.blit(ball, (i, 0))
    pygame.display.flip()
#    time.sleep(.00001)
raw_input()
