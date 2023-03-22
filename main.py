import pygame
from pygame.constants import QUIT

pygame.init()

screen = width, height = 1366, 700

BLACK = 0, 0, 0
WHITE = 255, 255, 255
pastel_colors = ((255, 183, 183), (183, 255, 183), (183, 183, 255), (255, 255, 183),
                 (255, 183, 255), (183, 255, 255), (255, 214, 183), (214, 255, 183),
                 (214, 183, 255), (255, 183, 214), (183, 255, 214), (183, 214, 255),
                 (255, 214, 214), (214, 255, 214), (214, 214, 255), (255, 255, 214),
                 (255, 214, 255), (214, 255, 255), (224, 112, 112), (112, 224, 112),
                 (112, 112, 224), (224, 224, 112), (224, 112, 224), (112, 224, 224),
                 (224, 168, 112), (168, 224, 112), (112, 168, 224), (224, 112, 168),
                 (112, 224, 168), (168, 112, 224), (224, 168, 168), (168, 224, 168))

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill((WHITE))
ball_rect = ball.get_rect()
ball_speed = [1, 1]

color_index = 0

is_working = True

while is_working:
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        color_index = (color_index + 1) % len(pastel_colors)
        ball.fill(pastel_colors[color_index])
    if ball_rect.right >= width or ball_rect.left <= 0:
        ball_speed[0] = -ball_speed[0]
        color_index = (color_index + 1) % len(pastel_colors)
        ball.fill(pastel_colors[color_index])

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)

    pygame.display.flip()

pygame.quit()
