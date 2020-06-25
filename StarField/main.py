import pygame
import time
import random

pygame.init()

HEIGHT, WIDTH = 500, 500
STARS = 50

screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('STARFIELD')

# Class star
class Star:
    def __init__(self):
        self.x = random.randint(100,400)
        self.y = random.randint(100,400)
        self.z = 0
        self.r = 0
        self.sx = (self.x - 250) // 10
        self.sy = (self.y - 250) // 10
        if abs(self.sx) + abs(self.sy) <= 20:
            if self.sx >= 0:
                self.sx += 5
            else:
                self.sx -= 5
            if self.sy >= 0:
                self.sy += 5
            else:
                self.sy -= 5
    def update(self):
        self.x += self.sx
        self.y += self.sy
        self.z += 1
        self.r = self.z // 5
        if (self.x < 0) or (self.x > 500) or (self.y < 0) or (self.y > 500):
            self.__init__()
    def show(self):
        pygame.draw.circle(screen, (225,225,225), (self.x, self.y), self.r)

star = []
for i in range(STARS):
    star.append(Star())

running = True
while running:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for i in range(STARS):
        star[i].update()
        star[i].show()

    time.sleep(0.05)
    pygame.display.update()