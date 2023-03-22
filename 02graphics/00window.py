import pygame

window = pygame.display.set_mode((800, 600))

pygame.draw.rect(window, (0, 255, 255), (200, 200, 400, 200))
pygame.draw.line(window, (255, 0, 255), (200, 500), (600, 100), 20)
pygame.draw.circle(window, (255, 255, 0), (400, 500), 50)
pygame.draw.ellipse(window, (255, 255, 255), (250, 50, 300, 100))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
