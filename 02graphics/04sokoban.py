import pygame
pygame.init()

TILE_SIZE = 64
LEVEL_WIDTH = 5
LEVEL_HEIGHT = 5

window = pygame.display.set_mode((
    LEVEL_WIDTH * TILE_SIZE,
    LEVEL_HEIGHT * TILE_SIZE
))
clock = pygame.time.Clock()

level = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 2, 0, 1],
    [1, 3, 3, 3, 1],
    [1, 1, 1, 1, 1]
]

position = (1, 2)
direction = 0

image = pygame.image.load("sokoban.png")

tiles = [
    (11, 6),    # 0 = floor
    (7, 6),     # 1 = wall
    (1, 0),     # 2 = box
    (10, 5),    # 3 = coin
    (3, 4),     # 4 = up
    (0, 6),     # 5 = right
    (0, 4),     # 6 = down
    (3, 6)      # 7 = left
]


def game_input():
    ...


def game_update():
    ...


def game_output():
    for y in range(0, LEVEL_HEIGHT):
        for x in range(0, LEVEL_WIDTH):
            draw_tile(0, x, y)
            draw_tile(level[y][x], x, y)
    draw_player()
    pygame.display.flip()


def draw_tile(tile, x, y):
    tx, ty = tiles[tile]
    position = (x * TILE_SIZE, y * TILE_SIZE)
    rectangle = (tx * TILE_SIZE, ty * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    window.blit(image, position, rectangle)


def draw_player():
    x, y = position
    draw_tile(4 + direction, x, y)


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(30)
