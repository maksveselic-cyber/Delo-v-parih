import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nyan Cat Game")

clock = pygame.time.Clock()


bg_color = (100, 120, 150)
ground_color = (80, 80, 80)


nyancat = pygame.image.load("nyancat.png")
nyancat = pygame.transform.scale(nyancat, (80, 80))

cat_x = WIDTH // 2 - 40
cat_y = HEIGHT // 2

velocity = 0
gravity = 0.8
jump_strength = -12


world_speed = 5


obstacles = []

def spawn_obstacle():
    x = WIDTH + 100
    y = HEIGHT - 100
    w = 40
    h = 60
    return pygame.Rect(x, y, w, h)


running = True
game_over = False

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                velocity = jump_strength

            if event.key == pygame.K_r and game_over:
               
                cat_y = HEIGHT // 2
                velocity = 0
                obstacles.clear()
                game_over = False

    if not game_over:
       
        velocity += gravity
        cat_y += velocity

     
        if cat_y > HEIGHT - 100:
            cat_y = HEIGHT - 100
            velocity = 0

     
        if random.randint(1, 60) == 1:
            obstacles.append(spawn_obstacle())

      
        for obs in obstacles:
            obs.x -= world_speed

      
        obstacles = [obs for obs in obstacles if obs.x > -50]

    
        cat_rect = pygame.Rect(cat_x, cat_y, 80, 80)
        for obs in obstacles:
            if cat_rect.colliderect(obs):
                game_over = True


    canvas.fill(bg_color)

  
    pygame.draw.rect(canvas, ground_color, (0, HEIGHT - 50, WIDTH, 50))

   
    for obs in obstacles:
        pygame.draw.rect(canvas, (200, 50, 50), obs)

    
    canvas.blit(nyancat, (cat_x, cat_y))

    
    if game_over:
        font = pygame.font.SysFont(None, 40)
        text = font.render("Game Over! Press R", True, (255, 255, 255))
        canvas.blit(text, (100, 200))

    pygame.display.update()

pygame.quit()
