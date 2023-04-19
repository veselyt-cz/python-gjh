import pygame
BOARD_SZE = 20
SQUARE_SIZE = 30
SQUARE_COLOR = (220, 220, 220)
SQUARE_HOVER_COLOR = (150, 150, 150)
CIRCLE_COLOR = (0, 255, 0)
CROSS_COLOR = (0, 0, 255)


board = []
for y in range(0, BOARD_SZE, 1):
    row = []
    for x in range(0, BOARD_SZE, 1):
        row.append(0)
    board.append(row)

current_square = (-1, -1)
player_turn = 1

window  = pygame.display.set_mode((BOARD_SZE*SQUARE_SIZE,BOARD_SZE*SQUARE_SIZE))


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_down()


def on_mouse_down():
    global player_turn
    x,y = current_square
    if board[y][x] ==0:
        board[y][x] = player_turn +1
        player_turn = (player_turn +1) % 2


def on_mouse_motion(event):
    global current_square
    mx,my = event.pos
    x = mx // SQUARE_SIZE
    y = my // SQUARE_SIZE
    current_square = x,y


def game_update():
    ...


def game_output():
    for y in range(0, BOARD_SZE, 1):
        for x in range(0, BOARD_SZE, 1):
            if current_square == (x, y):
                color = SQUARE_HOVER_COLOR
            else:
                color = SQUARE_COLOR
            pygame.draw.rect(window, color, (x * SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE-1, SQUARE_SIZE-1))

            if board[y][x] ==1:
                draw_o(x, y)
            if board[y][x] ==2:
                draw_x(x, y)
    pygame.display.flip()


def draw_o(x, y):
    pygame.draw.circle(window, CIRCLE_COLOR,
                       (x * SQUARE_SIZE + (SQUARE_SIZE/2),
                       y * SQUARE_SIZE + (SQUARE_SIZE / 2)), SQUARE_SIZE/2 -4, 4)


def draw_x(x, y):
    pygame.draw.line(window, CROSS_COLOR, (x*SQUARE_SIZE, y*SQUARE_SIZE), ((1+x)*SQUARE_SIZE, (1+y)*SQUARE_SIZE ), 3)
    pygame.draw.line(window, CROSS_COLOR, (x*SQUARE_SIZE, (y+1)*SQUARE_SIZE), ((x+1)*SQUARE_SIZE, y*SQUARE_SIZE), 3)
while True:
    game_input()
    game_update()
    game_output()
