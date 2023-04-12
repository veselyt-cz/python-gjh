import pygame

BOARD_SIZE = 20
SQUARE_SIZE = 30
SQUARE_COLOR = (255, 255, 255)
SQUARE_HOVER_COLOR = (225, 225, 225)

board = []

for y in range(0, BOARD_SIZE, 1):
    row = []
    for x in range(0, BOARD_SIZE, 1):
        row.append(0)
    board.append(row)

current = (-1, -1)

window = pygame.display.set_mode(
    (BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE)
)


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down()


def on_mouse_motion(event):
    global current
    mx, my = event.pos
    x = mx // SQUARE_SIZE
    y = my // SQUARE_SIZE
    current = x, y


def on_mouse_down():
    x, y = current
    board[y][x] = 1


def game_update():
    ...


def game_output():
    for y in range(0, BOARD_SIZE, 1):
        for x in range(0, BOARD_SIZE, 1):
            if current == (x, y):
                color = SQUARE_HOVER_COLOR
            else:
                color = SQUARE_COLOR
            pygame.draw.rect(window, color,
                             (x * SQUARE_SIZE, y * SQUARE_SIZE,
                              SQUARE_SIZE - 1, SQUARE_SIZE - 1))
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
