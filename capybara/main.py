import pygame as py
import random

py.init()

# game constants
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
WIDTH = 800
HEIGHT = 400

# game variables
score = 0
player_x = 50
player_y = 200
x_change = 0
y_change = 0
gravity = 1

screen = py.display.set_mode([WIDTH, HEIGHT])
py.display.set_caption("CapyGator")
background = black
fps = 60
font = py.font.Font('freesansbold.ttf', 16)
timer = py.time.Clock()

background = py.image.load('background.png')
background_rect = background.get_rect()

# load sprite image
player_sprite = py.image.load('capybara.png')
player_sprite = py.transform.scale(player_sprite, (70, 70)) # resize the sprite to 50x50 pixels
player_sprite = py.transform.flip(player_sprite, True, False)
player_rect = player_sprite.get_rect()


running = True
while running:
    timer.tick(fps)

    floor = py.draw.rect(screen, white, [0, 220, WIDTH, 5])
    # draw sprite
    player_rect.x = player_x
    player_rect.y = player_y
    screen.blit(background,background_rect)
    screen.blit(player_sprite, player_rect)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_w and y_change == 0:
                y_change = 15  # change how far up and down it jumps
            if event.key == py.K_d:
                x_change = 2
            if event.key == py.K_a:
                x_change = -2

        if event.type == py.KEYUP:
            if event.key == py.K_d:
                x_change = 0
            if event.key == py.K_a:
                x_change = 0

    if 0 <= player_x <= 430:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 430:
        player_x = 430

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    # boundary conditions
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_rect.width:
        player_x = WIDTH - player_rect.width
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_rect.height:
        player_y = HEIGHT - player_rect.height

    py.display.flip()

py.quit()