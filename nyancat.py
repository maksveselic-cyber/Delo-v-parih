import pygame

pygame.init()

canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption("moje prvo okno")

color = (100,120,150)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    canvas.fill(color)

    pygame.display.update()

pygame.quit()
