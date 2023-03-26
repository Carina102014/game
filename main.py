import pygame
import player
import gui
import time
import target
import tool
import random
import toolCostum


def main():
    pygame.init()
    my_screen=gui.GameGui("version 0.1.3")
    my_screen.build()
    clock = pygame.time.Clock()
    done=False

    image_target = pygame.image.load("target2.png")

    i=0

    vel = 1
    x = 200
    y = 127

    width = 40
    height = 40

    rosu = "red"
    verde = "green"
    galben = "yellow"
    albastru = "blue"

    id_1 = 1
    id_2 = 2
    id_3 = 3
    id_4 = 4

    cord_x1 = random.randint(50, 600)
    cord_y1 = random.randint(50, 600)
    cord_x2 = random.randint(50, 600)
    cord_y2 = random.randint(50, 600)
    cord_x3 = random.randint(50, 600)
    cord_y3 = random.randint(50, 600)
    cord_x4 = random.randint(50, 600)
    cord_y4 = random.randint(50, 600)

    id_color = random.randint(1,4)
    print(f"Initial id_color {id_color}")

    target_cord_x = 0
    target_cord_y = 0

    if id_color == 1:
        target_cord_x = cord_x1
        target_cord_y = cord_y1

    if id_color == 2:
        target_cord_x = cord_x2
        target_cord_y = cord_y2
    
    if id_color == 3:
        target_cord_x = cord_x3
        target_cord_y = cord_y3

    if id_color == 4:
        target_cord_x = cord_x4
        target_cord_y = cord_y4

    print(target_cord_x)
    print(target_cord_y)

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

        new_image_target = pygame.transform.scale(image_target, (width, height))
        my_screen.screen.blit(new_image_target, (x, y))

        target_1=target.Target("circle", albastru, cord_x1, cord_y1, 25, id_1)

        target_1.draw(surface = my_screen.screen)

        target_2=target.Target("circle", rosu, cord_x2, cord_y2, 25, id_2)
        target_2.draw(surface = my_screen.screen)
        
        target_3=target.Target("circle", verde, cord_x3, cord_y3, 25, id_3)
        target_3.draw(surface = my_screen.screen)

        target_4=target.Target("circle", galben, cord_x4, cord_y4, 25, id_4)
        target_4.draw(surface = my_screen.screen)

        # tool_1 = tool.Tool(id_color, x, y, width, height)
        # tool_1.build(my_screen.screen)

        tool_1 = toolCostum.ToolCostum(id_color, x, y, width, height)
        tool_1.build(my_screen.screen)

        if x <= target_cord_x + 20 and x >= target_cord_x - 20 and y >= target_cord_y - 22 and y <= target_cord_y - 10:

            print("shot")
            if id_color == 1:
                cord_x1 = random.randint(50, 600)
                cord_y1 = random.randint(50, 600)
                
                print(f"old {id_color}")
                id_color = random.randint(1,4)
                print(f"generated {id_color}")
                # print(f"Initial id_color {id_color}")

                if id_color == 1:
                    target_cord_x = cord_x1
                    target_cord_y = cord_y1

                elif id_color == 2:
                    target_cord_x = cord_x2
                    target_cord_y = cord_y2

                elif id_color == 3:
                    target_cord_x = cord_x3
                    target_cord_y = cord_y3
                
                elif id_color == 4:
                    target_cord_x = cord_x4
                    target_cord_y = cord_y4

                print(f"new x = {target_cord_x}")
                print(f"new y = {target_cord_y}")
            
            elif id_color == 2:
                cord_x2 = random.randint(50, 600)
                cord_y2 = random.randint(50, 600)

                print(f"old {id_color}")
                id_color = random.randint(1,4)
                print(f"generated {id_color}")
                # print(f"Initial id_color {id_color}")

                if id_color == 1:
                    target_cord_x = cord_x1
                    target_cord_y = cord_y1

                elif id_color == 2:
                    target_cord_x = cord_x2
                    target_cord_y = cord_y2

                elif id_color == 3:
                    target_cord_x = cord_x3
                    target_cord_y = cord_y3
                
                elif id_color == 4:
                    target_cord_x = cord_x4
                    target_cord_y = cord_y4

                print(f"new x = {target_cord_x}")
                print(f"new y = {target_cord_y}")

            elif id_color == 3:
                cord_x3 = random.randint(50, 600)
                cord_y3 = random.randint(50, 600)

                print(f"old {id_color}")
                id_color = random.randint(1,4)
                # print(f"Initial id_color {id_color}")
                print(f"generated {id_color}")


                if id_color == 1:
                    target_cord_x = cord_x1
                    target_cord_y = cord_y1

                elif id_color == 2:
                    target_cord_x = cord_x2
                    target_cord_y = cord_y2

                elif id_color == 3:
                    target_cord_x = cord_x3
                    target_cord_y = cord_y3
                
                elif id_color == 4:
                    target_cord_x = cord_x4
                    target_cord_y = cord_y4

                print(f"new x = {target_cord_x}")
                print(f"new y = {target_cord_y}")

            elif id_color == 4:
                cord_x4 = random.randint(50, 600)
                cord_y4 = random.randint(50, 600)

                print(f"old {id_color}")
                id_color = random.randint(1,4)
                print(f"generated {id_color}")
                # print(f"Initial id_color {id_color}")

                if id_color == 1:
                    target_cord_x = cord_x1
                    target_cord_y = cord_y1

                elif id_color == 2:
                    target_cord_x = cord_x2
                    target_cord_y = cord_y2

                elif id_color == 3:
                    target_cord_x = cord_x3
                    target_cord_y = cord_y3
                
                elif id_color == 4:
                    target_cord_x = cord_x4
                    target_cord_y = cord_y4

                print(f"new x = {target_cord_x}")
                print(f"new y = {target_cord_y}")

        pygame.display.update()
        
        clock.tick(300)

    pygame.quit()


if __name__ == "__main__":
    main()