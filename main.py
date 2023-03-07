import pygame
pygame.init
black=(0,0,0)
size=(700,700)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("My game")
clock=pygame.time.Clock()

class Player:
    def __init__ (self, name, age)
        

done=False

while done==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True


    screen.fill(black)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    

