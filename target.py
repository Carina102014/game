import pygame
import random

class Target:
    def __init__(self, shape, color, x, y, radius, id_target):
        self.shape = shape
        self.color = color
        self.position = [random.randint(0, 600), random.randint(0, 500)]
        self.radius = radius
        self.x = x
        self.y = y
        self.radius=radius
        self.id_target = id_target
    
    def draw(self, surface):
        if(self.shape == "circle"):

            pygame.draw.circle(surface, self.color, (self.x,self.y), self.radius, 0)

     