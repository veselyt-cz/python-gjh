import pygame

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()

SIZE = 100

x = 350
y = 250
dx = 1
dy = 1
v = 0.1
a = 0.01

while True:
    # 1. INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 2. UPDATE
    x += 2 * v * dx
    y += v * dy
    v += a
    if x <= 0 or x >= window.get_width() - SIZE:
        dx = -dx
    if y <= 0 or y >= window.get_height() - SIZE:
        dy = -dy
    if v < -10 or v > 10:
        a = -a
    # 3. OUTPUT
    window.fill((255, 255, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, SIZE, SIZE))
    pygame.display.flip()
    clock.tick(60)
