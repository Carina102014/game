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

        #surface = the screen
        # self.color = what color will have the shape
        # (122, 250) = coordonates -> x = 122 and y=250
        # 20 = radius of the circle
        # 0 = fill with color all the circle
        pygame.draw.circle(surface, self.color, (122,250), 20, 0)
        pygame.display.flip()
    
     