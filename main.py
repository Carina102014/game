import pygame
import player
import gui
import time
import target


def main():
    pygame.init()
    my_screen=gui.GameGui("version 0.0.1")
    my_screen.build()
    # player_one = player.Player(name="Carina", age=20)
    # player_one.tool.build(my_screen.screen)
    # time.sleep(4)
    # player_one.tool.change_color("red")
    # player_one.tool.draw_tool(my_screen.screen, 80, 80)
    # time.sleep(4)
    # target_1=target.Target()
    # target_1.draw(surface = my_screen.screen)
    # time.sleep(4)

    done=False

    vel = 1
    x = 100
    y = 200

    width = 20
    height = 20


    while done==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel

        if keys[pygame.K_RIGHT] and x < 700 - width:
            x += vel
        
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        
        if keys[pygame.K_DOWN] and y < 700 - height:
            y += vel

        my_screen.screen.fill((0,0,0))
        target_1=target.Target("circle", "red", 200, 150)
        target_1.draw(surface = my_screen.screen)

        target_2=target.Target("rect", "green", 300, 350)
        target_2.draw(surface = my_screen.screen)

        pygame.draw.rect(my_screen.screen, "white", (50,50,100,100))
        # pygame.display.flip()

        pygame.draw.rect(my_screen.screen, "blue", (x,y, width, height))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()