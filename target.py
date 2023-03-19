import pygame
import random


class Target:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.position = [random.randint(0, 600), random.randint(0, 500)]
        self.radius = 10
        self.x = x
        self.y = y
    
    def draw(self, surface):
        # surface.fill((0,0,0))

        #surface = the screen
        # self.color = what color will have the shape
        # (122, 250) = coordonates -> x = 122 and y=250
        # 20 = radius of the circle
        # 0 = fill with color all the circle
        if(self.shape == "circle"):
            pygame.draw.circle(surface, self.color, (self.x,self.y), 20, 0)

    
     