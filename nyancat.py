import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("moje prvo okno")

color = (100,120,150)

nyancat = pygame.image.load("nyancat.png")
nyancat = pygame.transform.scale(nyancat, (80, 80))

clock = pygame.time.Clock()


cat_x = WIDTH // 2 - 40
cat_y = HEIGHT // 2 - 40


world_x = 0
speed = 5

running = True

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    world_x -= speed

    canvas.fill(color)

   
    for i in range(0, 1000, 100):
        pygame.draw.rect(canvas, (255, 255, 255), (i + world_x, 300, 50, 20))

   
    canvas.blit(nyancat, (cat_x, cat_y))

    pygame.display.update()

pygame.quit()
