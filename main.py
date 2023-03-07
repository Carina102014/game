import pygame
import gui


def main():
    pygame.init()
    my_screen=gui.GameGui("version 0.0.1")

    done=False

    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True

    my_screen.build()
    my_screen.set_clock(60)
     



if __name__ == "__main__":
    main()