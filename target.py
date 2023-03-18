import pygame
import random


class Target:
    def __init__(self):
        self.shape = "circle"
        self.color = "green"
        self.position = [random.randint(0, 600), random.randint(0, 500)]
        self.radius = 10
    
    def draw(self, surface):
        surface.fill((0,0,0))
        pygame.draw.circle(surface, self.color, pygame.Rect(self.position, self.radius))
        pygame.display.flip()
    
     