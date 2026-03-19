import pygame

pygame.init()

canvas = pygame.display.set_mode((500, 500))
pygame.display.set_caption("moje prvo okno")

color = (100,120,150)

nyancat = pygame.image.load("nyancat.png")
nyancat = pygame.transform.scale(nyancat, (80, 80))

clock = pygame.time.Clock()
x = 100
y = 100
hitrost = 5

running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 👇 NEW: keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= hitrost
    if keys[pygame.K_RIGHT]:
        x += hitrost
    if keys[pygame.K_UP]:
        y -= hitrost
    if keys[pygame.K_DOWN]:
        y += hitrost

    canvas.fill(color)
    canvas.blit(nyancat, (x, y))

    pygame.display.update()

pygame.quit()
