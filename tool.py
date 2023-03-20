import pygame

class Tool():
    def __init__(self, color, x, y, width, height):
        self.shape = "rect"
        self.color = color
        self.size = (30, 30)
        self.position = (60, 60)
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def build(self, screen):
        if self.shape == "rect":    
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            # pygame.display.flip()

    def change_color(self, new_color):
        self.color = new_color

    def draw_tool(self, screen, x, y):
        screen.fill((0,0,0))
        self.position = (x, y)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position, self.size))
        # pygame.display.flip()


