import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_pos = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_pos()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
food = snake.copy()
food.center = get_random_pos()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                    snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                    snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                    snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_d:
                    snake_dir = (TILE_SIZE, 0)
    screen.fill('black')
    # check 4 food
    if snake.center == food.center:
          food.center = get_random_pos()
          length += 1
    # foodies yummers
    pg.draw.rect(screen, 'red', food)
    # draw snake
    [pg.draw.rect(screen, 'green', segment) for segment in segments]
    # snakey move
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
          time = time_now
          snake.move_ip(snake_dir)
          segments.append(snake.copy())
          segments = segments[+length:]
    pg.display.flip()
    clock.tick(60)        