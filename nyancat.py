import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nyan Cat Platform Game")

clock = pygame.time.Clock()

bg_color = (100, 120, 150)
ground_color = (80, 80, 80)

nyancat = pygame.image.load("nyancat.png").convert()
nyancat.set_colorkey((255, 255, 255))
nyancat = pygame.transform.scale(nyancat, (60, 60))

font = pygame.font.SysFont("arial", 30)

velocity = 0
gravity = 0.8
jump_strength = -12

world_speed = 5

score = 0
high_score = 0
rainbow = []
platforms = []
zvezdice = []

def spawn_platform():
    x = WIDTH + 50
    y = random.randint(200, HEIGHT - 120)
    w = random.randint(80, 140)
    h = 15
    return pygame.Rect(x, y, w, h)

def spawn_zvezdica():
    x = WIDTH + 50
    y = random.randint(100, HEIGHT - 200)
    return pygame.Rect(x, y, 30, 30)

cat_x = WIDTH // 2 - 30
cat_y = HEIGHT // 2

running = True
game_over = False

while running:

    clock.tick(45)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not game_over:
                velocity = jump_strength

            if event.key == pygame.K_r and game_over:
                cat_y = HEIGHT // 2
                velocity = 0
                platforms.clear()
                rainbow.clear()
                zvezdice.clear()
                score = 0
                game_over = False

    if not game_over:
        velocity += gravity
        cat_y += velocity

        if random.randint(1, 50) == 1:
            platforms.append(spawn_platform())

        if random.randint(1, 80) == 1:
            zvezdice.append(spawn_zvezdica())

        current_speed = world_speed + score * 0.05

        for p in platforms:
            p.x -= current_speed

        for z in zvezdice:
            z.x -= current_speed

        platforms = [p for p in platforms if p.x > -100]
        zvezdice = [z for z in zvezdice if z.x > -50]

        cat_rect = pygame.Rect(cat_x, cat_y, 60, 60)

        m = 5

        for p in platforms:
            if velocity > 0:
                if cat_rect.bottom + velocity >= p.top and cat_rect.bottom <= p.top + m:
                    if cat_rect.right > p.left + 5 and cat_rect.left < p.right - 5:
                        cat_y = p.top - 60
                        velocity = 0
                        score += 1
                        
        for z in zvezdice:
            if cat_rect.colliderect(z):
                score += 5
                zvezdice.remove(z)

        if cat_y > HEIGHT:
            game_over = True
        if score > high_score:
            high_score = score

        if rainbow:
            prejsnji = rainbow[-1]
            cx = cat_x - prejsnji[0]
            cy = cat_y - prejsnji[1]

            for i in range(4):
                x = prejsnji[0] + cx * i / 4
                y = prejsnji[1] + cy * i / 4
                rainbow.append([x, y])
        else:
            rainbow.append([cat_x, cat_y])

    for i in rainbow:
        i[0] -= world_speed

    if len(rainbow) > 300:
        rainbow.pop(0)

    rainbow = [i for i in rainbow if i[0] > -50]

    canvas.fill(bg_color)

    for p in platforms:
        pygame.draw.rect(canvas, (200, 200, 200), p)

    for z in zvezdice:
        pygame.draw.circle(canvas, (255, 255, 0), z.center, 8)

    barve = [(255,0,0),(255,255,0),(0,255,0),(0,0,255)]

    for i in rainbow:
        for j in range(4):
            pygame.draw.circle(canvas, barve[j], (int(i[0]), int(i[1] + j*5)), 4)

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    canvas.blit(score_text, (10, 10))

    high_score_text = font.render(f"High: {high_score}", True, (255,0,0))
    canvas.blit(high_score_text, (10, 40))

    if game_over:
        text = font.render("Game Over! Press R", True, (255, 255, 255))
        canvas.blit(text, (100, 200))

    canvas.blit(nyancat, (cat_x, cat_y))
    pygame.display.update()

pygame.quit()