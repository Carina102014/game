import pygame

class GameGui():
    def __init__(self,version):
       self.color=(0,0,0) 
       self.size=(700,700)
       clock=pygame.time.Clock()


    def build(self):
        self.screen=pygame.display.set_mode(self.size)
        pygame.display.set_caption("My game")
        self.screen.fill(0,0,0)
        pygame.display.flip()

    
    def set_clock(self,new_clock):
        self.clock=new_clock
 

 

        

 