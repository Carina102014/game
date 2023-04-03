import pygame
import player
import gui
import time
import target
import tool
import random
import toolCostum
import button
import logging


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    pygame.init()
    my_screen=gui.GameGui("version 0.1.3")
    my_screen.build()
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    done=False

# ------- music / sound ------------------------------
    target_sound =  pygame.mixer.Sound("sounds/sound_shot.mp3") 
    click_sound = pygame.mixer.Sound("sounds/sound_click.wav")

#  ------  images ---------------------------------
    image_target = pygame.image.load("images/target2.png")
    image_start = pygame.image.load("images/start.png")
    image_exit = pygame.image.load("images/exit.png")
    image_continue = pygame.image.load("images/continue.png")
    image_new_game = pygame.image.load("images/new_game.jpg")
    image_quit = pygame.image.load("images/quit.jpg")

# ------ variable score ---------------------
    score = 0

# variables for timer ------------------------
    timer = 10
    last_timer = pygame.time.get_ticks()

    timer_bonus = 5
    last_timer_bonus = pygame.time.get_ticks()

# input_name variables -----------------------
    user_name = ""
    input_name = pygame.Rect(190,450,140,50)
    color_active = pygame.Color("blue")
    color_passive = pygame.Color("red")
    color = color_passive

    active = False
# ------------ variables for the game windows --------------------
    game_start = True
    game_paused = False
    state_start = False
    finish_game = False
    save_game = False
    quit_game = False

# --------- variables for the TOOL -------------
    vel = 1
    x = 200
    y = 127

    width = 40
    height = 40

# ---------- colors -----------------
    red = "red"
    green = "green"
    yellow = "yellow"
    blue = "blue"

# ------- targets ids -----------------------
    id_1 = 1
    id_2 = 2
    id_3 = 3
    id_4 = 4

# -------------- targets coordonates ----------------------
    cord_x1 = random.randint(50, 600)
    cord_y1 = random.randint(170, 600)
    cord_x2 = random.randint(50, 600)
    cord_y2 = random.randint(170, 600)
    cord_x3 = random.randint(50, 600)
    cord_y3 = random.randint(170, 600)
    cord_x4 = random.randint(50, 600)
    cord_y4 = random.randint(170, 600)

# ------- generate a random color for the TOOL and set the value of target_cord_x and target_cord_y ---------
    id_color = random.randint(1,4)
    logging.debug(f"Inital id_color is {id_color}")

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

    logging.debug(f"target_cord_x = {target_cord_x}")
    logging.debug(f"target_cord_y = {target_cord_y}")

    buton_start = button.Button(250, 200, image_start, 0.4)
    buton_exit = button.Button(250,300, image_exit, 0.4)
    buton_continue = button.Button(250,200, image_continue, 0.4)
    buton_save = button.Button(250, 300, image_new_game, 0.4)
    buton_quit = button.Button(250, 400, image_quit, 0.4)


    while done==False:

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_name.collidepoint(event.pos):
                    active = True
                
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_name = user_name[0:-1]
                    else:
                        user_name += event.unicode

                if event.key == pygame.K_p:
                    game_paused = True
                    logging.debug(f"game_paused = {game_paused}")

                if event.key == pygame.K_s:
                    game_paused = False
                    logging.debug(f"game_paused = {game_paused}")

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

        if game_start == True:
            state_start = buton_start.draw(my_screen.screen)
            state_exit = buton_exit.draw(my_screen.screen)

            if active:
                color = color_active
            
            else:
                color = color_passive

            text_surface = my_font.render(f'Name', False, (255, 255, 255))
            my_screen.screen.blit(text_surface, (300,400))

            name_surface = my_font.render(user_name, True, (255,255,255))
            my_screen.screen.blit(name_surface, (input_name.x + 5, input_name.y + 5))

            input_name.w = max(300, name_surface.get_width() + 10)
            pygame.draw.rect(my_screen.screen, color, input_name, 2)


            if state_start:
                click_sound.play()
                print("start")
                timer = 10
                score = 0
                game_paused = False
                game_start = False

            if state_exit:
                print("exit")
                done=True

        # show the finish menu ---------------------------------------------------------------
        elif  finish_game == True:
                text_surface = my_font.render(f'The game finish', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (220,20))

                text_surface = my_font.render(f'Congratulations {user_name}', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (170,100))

                text_surface = my_font.render(f'Your score is: {score}', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (210,200))

                save_game = buton_save.draw(my_screen.screen)
                quit_game = buton_quit.draw(my_screen.screen)

                if save_game:
                    print("game saved")
                    print(user_name)
                    print(score)
                    file = open('player.txt', 'w')
                    file.write(user_name + "\n")
                    file.write(str(score)+"\n")
                    file.close()
                    game_start = True
                    finish_game = False

                if quit_game:
                    print("game quited")
                    print(user_name)
                    print(score)
                    file = open('player.txt', 'w')
                    file.write(user_name + "\n")
                    file.write(str(score)+"\n")
                    file.close()
                    done = True
        # ------------------------------------------------------------------------------------

        else:

            if game_paused == False:

                new_image_target = pygame.transform.scale(image_target, (width, height))
                my_screen.screen.blit(new_image_target, (x, y))

                text_surface = my_font.render(f'Score: {score}', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (20,20))

                text_surface = my_font.render(f'Timer: {timer}', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (200,20))

                text_surface = my_font.render(f'Player: {user_name}', False, (255, 255, 255))
                my_screen.screen.blit(text_surface, (400,20))

                target_1=target.Target("circle", blue, cord_x1, cord_y1, 25, id_1)

                target_1.draw(surface = my_screen.screen)

                target_2=target.Target("circle", red, cord_x2, cord_y2, 25, id_2)
                target_2.draw(surface = my_screen.screen)
                
                target_3=target.Target("circle", green, cord_x3, cord_y3, 25, id_3)
                target_3.draw(surface = my_screen.screen)

                target_4=target.Target("circle", yellow, cord_x4, cord_y4, 25, id_4)
                target_4.draw(surface = my_screen.screen)

                tool_1 = toolCostum.ToolCostum(id_color, x, y, width, height)
                tool_1.build(my_screen.screen)

                if x <= target_cord_x + 20 and x >= target_cord_x - 20 and y >= target_cord_y - 22 and y <= target_cord_y - 10:

                    logging.debug("shot")
                    target_sound.play()
                    if id_color == 1:
                        score = score + 1
                        cord_x1 = random.randint(50, 600)
                        cord_y1 = random.randint(170, 600)

                        # bonus timer -------------------------------
                        if timer != 0:
                            if timer_bonus == 5:
                                timer_bonus = 5
                                timer = timer + 4
                                logging.debug(f"timer = {timer} + 4")
                            elif timer_bonus == 4:
                                timer_bonus = 5
                                timer = timer + 3
                                logging.debug(f"timer = {timer} + 3")
                            else:
                                timer_bonus = 5
                                timer = timer + 2
                                logging.debug(f"timer = {timer} + 2")
                        
                        logging.debug(f"old id_color = {id_color}")
                        id_color = random.randint(1,4)
                        logging.debug(f"new id_color = {id_color}")

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

                        logging.debug(f"new target_cord_x = {target_cord_x}")
                        logging.debug(f"new target_cord_y = {target_cord_y}")
                    
                    elif id_color == 2:
                        score = score + 1
                        cord_x2 = random.randint(50, 600)
                        cord_y2 = random.randint(170, 600)

                        # bonus timer -------------------------------
                        if timer != 0:
                            if timer_bonus == 5:
                                timer_bonus = 5
                                timer = timer + 4
                                logging.debug(f"timer = {timer} + 4")
                            elif timer_bonus == 4:
                                timer_bonus = 5
                                timer = timer + 3
                                logging.debug(f"timer = {timer} + 3")
                            else:
                                timer_bonus = 5
                                timer = timer + 2
                                logging.debug(f"timer = {timer} + 2")

                        logging.debug(f"old id_color = {id_color}")
                        id_color = random.randint(1,4)
                        logging.debug(f"new id_color = {id_color}")

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

                        logging.debug(f"new target_cord_x = {target_cord_x}")
                        logging.debug(f"new target_cord_y = {target_cord_y}")

                    elif id_color == 3:
                        score = score + 1
                        cord_x3 = random.randint(50, 600)
                        cord_y3 = random.randint(170, 600)

                        # bonus timer -------------------------------
                        if timer != 0:
                            if timer_bonus == 5:
                                timer_bonus = 5
                                timer = timer + 4
                                logging.debug(f"timer = {timer} + 4")
                            elif timer_bonus == 4:
                                timer_bonus = 5
                                timer = timer + 3
                                logging.debug(f"timer = {timer} + 3")
                            else:
                                timer_bonus = 5
                                timer = timer + 2
                                logging.debug(f"timer = {timer} + 2")

                        logging.debug(f"old id_color = {id_color}")
                        id_color = random.randint(1,4)
                        logging.debug(f"new id_color = {id_color}")

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

                        logging.debug(f"new target_cord_x = {target_cord_x}")
                        logging.debug(f"new target_cord_y = {target_cord_y}")

                    elif id_color == 4:
                        score = score + 1
                        cord_x4 = random.randint(50, 600)
                        cord_y4 = random.randint(170, 600)

                        # bonus timer -------------------------------
                        if timer != 0:
                            if timer_bonus == 5:
                                timer_bonus = 5
                                timer = timer + 4
                                logging.debug(f"timer = {timer} + 4")
                            elif timer_bonus == 4:
                                timer_bonus = 5
                                timer = timer + 3
                                logging.debug(f"timer = {timer} + 3")
                            else:
                                timer_bonus = 5
                                timer = timer + 2
                                logging.debug(f"timer = {timer} + 2")
                         

                        logging.debug(f"old id_color = {id_color}")
                        id_color = random.randint(1,4)
                        logging.debug(f"new id_color = {id_color}")

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

                        logging.debug(f"new target_cord_x = {target_cord_x}")
                        logging.debug(f"new target_cord_y = {target_cord_y}")

                if timer == 0:
                    finish_game = True

                # timer -----------------------------------------------
                if timer > 0:
                    count_timer = pygame.time.get_ticks()
                    if count_timer - last_timer > 1000:
                        timer = timer - 1
                        last_timer = count_timer

                # timer_bonus --------------------------------------------
                if timer_bonus > 0:
                    count_timer_bonus = pygame.time.get_ticks()
                    if count_timer_bonus - last_timer_bonus > 1000:
                        timer_bonus = timer_bonus - 1
                        last_timer_bonus = count_timer_bonus

            else:
                state_continue = buton_continue.draw(my_screen.screen)
                state_exit = buton_exit.draw(my_screen.screen)

                if state_exit:
                    done = True

                if state_continue:
                    click_sound.play()
                    game_paused = False


        pygame.display.update()
        clock.tick(270)

    pygame.quit()


if __name__ == "__main__":
    main()