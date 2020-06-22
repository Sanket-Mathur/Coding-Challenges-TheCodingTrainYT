import pygame
import random
import time
from pygame import mixer

pygame.init()

SCREENX, SCREENY = 640, 360
DROPS = 500

screen = pygame.display.set_mode((SCREENX, SCREENY))
pygame.display.set_caption('PURPLE RAIN')

# Sound of rain playing in a loop
mixer.music.load('Rain_Sound.wav')
mixer.music.play(-1)

# Class drop containing all the properties of a drop
class Drop:
    def __init__(self):
        self.x = random.randint(0, SCREENX)
        self.y = random.randint(-200,-20)
        self.z = random.randint(0,20)
        self.speed = random.randint(3,10)
        self.length = random.randint(10,20)
        if 0 <= self.z < 7:
            self.gravity = 0.05
            self.width = 0
        elif 7 <= self.z < 14:
            self.gravity = 0.1
            self.width = 1
        else:
            self.gravity = 0.2
            self.width = 2

    def fall(self):
        self.y += self.speed
        self.speed += self.gravity
        if self.y > 360:
            self.y = random.randint(-200,-20)
            self.speed = random.randint(5,10)
        if 360-self.length < self.y <= 360:
            pygame.draw.line(screen, (138, 43, 226), (self.x, 360), (self.x - 5 , 350))
            pygame.draw.line(screen, (138, 43, 226), (self.x, 360), (self.x + 5 , 350))

    def show(self):
        pygame.draw.rect(screen, (138, 43, 226), pygame.Rect(self.x, self.y, self.width, self.length))

# Initializing DROPS number of drops
drop = []
for i in range(DROPS):
    drop.append(Drop())

# Execution Loop
running = True
while running:

    screen.fill((230, 230, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(DROPS):
        drop[i].fall()
        drop[i].show()
    
    pygame.display.update()
    time.sleep(0.01)