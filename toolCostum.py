import pygame
import random

class ToolCostum():
    def __init__(self, id_color, x, y, width, height):
        self.id_color = id_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def build(self, screen):
        if self.id_color == 1:
           self.image = pygame.image.load("images/target1.png")
        
        elif self.id_color == 2:
           self.image = pygame.image.load("images/target3.png")
        
        elif self.id_color == 3:
           self.image = pygame.image.load("images/target2.png")
        
        elif self.id_color == 4:
           self.image = pygame.image.load("images/target4.png")

        new_iamge = pygame.transform.scale(self.image, (self.width, self.height))

        screen.blit(new_iamge, (self.x, self.y))

    def change_color(self, new_color):
        self.color = new_color

    def draw_tool(self, screen, x, y):
        screen.fill((0,0,0))
        self.position = (x, y)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position, self.size))


