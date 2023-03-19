import pygame

class GameGui():
    def __init__(self,version):
       self.color=(0,0,0) 
       self.size=(700,700)
       self.clock=pygame.time.Clock()
       self.version = version
       

    def build(self):
        self.screen=pygame.display.set_mode(self.size)
        pygame.display.set_caption(f"My game {self.version}")
        self.set_clock(200)
        self.screen.fill((0,0,0))

    
    def set_clock(self,new_clock):
        self.clock.tick(new_clock) 

 

        

 