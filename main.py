import pygame
import player
import gui
import time


def main():
    pygame.init()
    my_screen=gui.GameGui("version 0.0.1")
    my_screen.build()
    player_one = player.Player(name="Carina", age=20)
    player_one.tool.build(my_screen.screen)
    time.sleep(5)
    player_one.tool.change_color("red")
    player_one.tool.draw_tool(my_screen.screen, 80, 80)

    done=False

    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()