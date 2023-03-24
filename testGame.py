import pygame, sys

pygame.init()

SCREEN = pygame.display.set_mode((700,700))

# ---- Colors ------

WHITE = (255,255,255)
DARK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

pygame.display.set_caption("First Game")
SCREEN.fill(DARK)

pygame.draw.rect(SCREEN, "red", (50, 50, 40, 40))

pygame.draw.line(SCREEN, BLUE, (100,70), (200,70), 10)

pygame.draw.circle(SCREEN, GREEN, (250, 70), 20, 0)

pygame.draw.ellipse(SCREEN, WHITE, (350, 70, 40, 80))

puncts = [(180,300), (180,100), (50,100)]

pygame.draw.polygon(SCREEN, RED, puncts, 8)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()



    # ----------------------------------
        #     target_1=target.Target("circle", "red", 200, 150)
        # target_1.draw(surface = my_screen.screen)

        # target_2=target.Target("rect", "green", 300, 350)
        # target_2.draw(surface = my_screen.screen)

        # pygame.draw.rect(my_screen.screen, "white", (50,50,100,100))
        # # pygame.display.flip()