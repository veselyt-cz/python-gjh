import pygame

BOARD_SIZE = 20
SQUARE_SIZE = 30
SQUARE_COLOR = (255, 255, 255)
SQUARE_HOVER_COLOR = (225, 225, 225)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)

board = []

for y in range(0, BOARD_SIZE, 1):
    row = []
    for x in range(0, BOARD_SIZE, 1):
        row.append(0)
    board.append(row)

current = (-1, -1)
player = 1

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
    global player
    x, y = current
    if board[y][x] == 0:
        board[y][x] = player + 1
        player = (player + 1) % 2


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
            if board[y][x] == 1:
                draw_o(x, y)
            if board[y][x] == 2:
                draw_x(x, y)
    pygame.display.flip()


def draw_o(x, y):
    pygame.draw.circle(window, CIRCLE_COLOR, (
        x * SQUARE_SIZE + SQUARE_SIZE // 2,
        y * SQUARE_SIZE + SQUARE_SIZE // 2
    ), SQUARE_SIZE // 2 - 4, 4)


def draw_x(x, y):
    pygame.draw.line(window, CROSS_COLOR,
                     (x * SQUARE_SIZE, y * SQUARE_SIZE),
                     ((x + 1) * SQUARE_SIZE, (y + 1) * SQUARE_SIZE), 4)
    pygame.draw.line(window, CROSS_COLOR,
                     (x * SQUARE_SIZE, (y + 1) * SQUARE_SIZE),
                     ((x + 1) * SQUARE_SIZE, y * SQUARE_SIZE), 4)


while True:
    game_input()
    game_update()
    game_output()
