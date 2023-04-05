import pygame

BACKGROUND_COLOR = (0, 0, 0)
PADDLE_COLOR = (255, 255, 255)
PADDLE_WIDTH = 30
PADDLE_HEIGHT = 200
BALL_COLOR = (255, 255, 255)
BALL_SIZE = 10
WINDOW_HEIGHT = 600

left_paddle_x = 20
left_paddle_y = 200
left_paddle_dy = 0
right_paddle_x = 750
right_paddle_y = 200
right_paddle_dy = 0

ball_x = 400
ball_y = 300
ball_dx = 1
ball_dy = 1

window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event)
        elif event.type == pygame.KEYUP:
            on_key_up(event)


def on_key_down(event):
    global left_paddle_dy, right_paddle_dy
    if event.key == pygame.K_UP:
        right_paddle_dy = -1
    elif event.key == pygame.K_DOWN:
        right_paddle_dy = 1
    elif event.key == pygame.K_w:
        left_paddle_dy = -1
    elif event.key == pygame.K_s:
        left_paddle_dy = 1


def on_key_up(event):
    global left_paddle_dy, right_paddle_dy
    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        right_paddle_dy = 0
    elif event.key == pygame.K_w or event.key == pygame.K_s:
        left_paddle_dy = 0


def game_update():
    global left_paddle_y, right_paddle_y, ball_x, ball_y, ball_dx, ball_dy
    left_paddle_y += 10 * left_paddle_dy
    right_paddle_y += 10 * right_paddle_dy
    ball_x += 5 * ball_dx
    ball_y += 5 * ball_dy
    if ball_y <= 0 + BALL_SIZE:
        ball_dy = 1
    if ball_y >= WINDOW_HEIGHT - BALL_SIZE:
        ball_dy = -1
    if ball_x + BALL_SIZE >= right_paddle_x:
        if ball_y + BALL_SIZE > right_paddle_y \
                and ball_y - BALL_SIZE < right_paddle_y + PADDLE_HEIGHT:
            ball_dx = -1
    if ball_x - BALL_SIZE <= left_paddle_x + PADDLE_WIDTH:
        if ball_y + BALL_SIZE > left_paddle_y \
                and ball_y - BALL_SIZE < left_paddle_y + PADDLE_HEIGHT:
            ball_dx = 1


def game_output():
    window.fill(BACKGROUND_COLOR)
    pygame.draw.rect(window, PADDLE_COLOR,
                     (left_paddle_x, left_paddle_y,
                      PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(window, PADDLE_COLOR,
                     (right_paddle_x, right_paddle_y,
                      PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(window, BALL_COLOR,
                       (ball_x, ball_y), BALL_SIZE)
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
    clock.tick(30)
