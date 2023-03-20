import pygame
import player
import gui
import time
import target
import tool
import random


def main():
    pygame.init()
    my_screen=gui.GameGui("version 0.1.3")
    my_screen.build()
    clock = pygame.time.Clock()
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

    i=0

    vel = 1
    x = 200
    y = 127

    width = 40
    height = 40

    diametru = 20

    culoare = "blue"

    rosu = "red"
    verde = "green"
    galben = "yellow"
    albastru = "blue"

    cord_x = random.randint(50, 600)
    cord_y = random.randint(50, 600)
    cord_x1 = random.randint(50, 600)
    cord_y1 = random.randint(50, 600)
    cord_x2 = random.randint(50, 600)
    cord_y2 = random.randint(50, 600)

    print(cord_x2)
    print(cord_y2)

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

        target_1=target.Target("circle", rosu, cord_x, cord_y, 10)

        target_1.draw(surface = my_screen.screen)

        target_2=target.Target("circle", albastru, cord_x1, cord_y1, 25)
        target_2.draw(surface = my_screen.screen)
        
        target_3=target.Target("circle", galben, cord_x2, cord_y2, diametru)
        target_3.draw(surface = my_screen.screen)
        target_4=target.Target("circle", albastru, 500, 500, 20)
        target_4.draw(surface = my_screen.screen)

        # pygame.draw.rect(my_screen.screen, culoare, (x,y, width, height))
        tool_1 = tool.Tool(culoare, x, y, width, height)
        tool_1.build(my_screen.screen)

        if x <= cord_x1 + 20 and x >= cord_x1 - 20 and y >= cord_y1 - 22 and y <= cord_y1 - 10:
            if culoare == target_2.color:
                print("compatibil")
                cord_x1 = random.randint(50, 600)
                cord_y1 = random.randint(50, 600)

            print("shot")

        # if x <= 520 and x >= 480 and y >= 478 and y <= 490 and diametru * 2 == width:
        #     print("lovit" + str(i))
        #     i = i + 1
            # print(target_4.color)

        pygame.display.update()
        
        clock.tick(300)

    pygame.quit()


if __name__ == "__main__":
    main()