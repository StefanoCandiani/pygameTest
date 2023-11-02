import pygame
import random

pygame.init()

screen_height = int(input('Please provide a screen height: '))
screen_width = int(input('Please provide a screen width: '))
x_pos = screen_width/2
y_pos = screen_height/2

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Mamma Mia Game')


running = True
while running:
    pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_pos, y_pos, 25, 25))
    for event in pygame.event.get():
        pass
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed()

    if button[pygame.K_LEFT]:
        x_pos -= 0.5
        if(x_pos < 0):
            x_pos = screen_width

    if button[pygame.K_RIGHT]:
        x_pos += 0.5
        if(x_pos > screen_width):
            x_pos = 0

    if button[pygame.K_DOWN]:
        y_pos += 0.5
        if (y_pos > screen_height):
            y_pos = 0

    if button[pygame.K_UP]:
        y_pos -= 0.5
        if (y_pos < 0):
            y_pos = screen_height

    pygame.display.flip()