import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
<<<<<<< HEAD
pygame.display.set_caption("Nyan Cat Game")

clock = pygame.time.Clock()


bg_color = (100, 120, 150)
ground_color = (80, 80, 80)
=======
>>>>>>> d8a5a44167dcf42a4598f7809b16e32e197dc5d9
pygame.display.set_caption("moje prvo okno")

color = (100,120,150)

nyancat = pygame.image.load("nyancat.png")
nyancat = pygame.transform.scale(nyancat, (80, 80))

cat_x = WIDTH // 2 - 40
cat_y = HEIGHT // 2

velocity = 0
gravity = 0.8
jump_strength = -12


world_speed = 5
clock = pygame.time.Clock()

<<<<<<< HEAD
rainbow = []
obstacles = []
cat_x = WIDTH // 2 - 40
cat_y = HEIGHT // 2 - 40

def spawn_obstacle():
    x = WIDTH + 100
    y = HEIGHT - 100
    w = 40
    h = 60
    return pygame.Rect(x, y, w, h)
=======

cat_x = WIDTH // 2 - 40
cat_y = HEIGHT // 2 - 40

>>>>>>> d8a5a44167dcf42a4598f7809b16e32e197dc5d9

world_x = 0
speed = 5

running = True
game_over = False

while running:
    clock.tick(45)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

<<<<<<< HEAD
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

    world_x -= speed

    canvas.fill(bg_color)

  
    pygame.draw.rect(canvas, ground_color, (0, HEIGHT - 50, WIDTH, 50))
    


    for obs in obstacles:
        pygame.draw.rect(canvas, (200, 50, 50), obs)
    barve = [
        (255,0,0),
        (255,255,0),
        (0,255,0),
        (0,0,255),
        ]
    for i in rainbow:
        for j in range(4):
            pygame.draw.rect(canvas, barve[j], (i[0], i[1] + j*8, 50,8))

    rainbow.append([cat_x, cat_y])
    for i in rainbow:
        i[0] -= world_speed
        i[1] += 0.5
    rainbow = [i for i in rainbow if i[0] > -100]   

    for i in range(0, 1000, 100):
        pygame.draw.rect(canvas, (255, 255, 255), (i + world_x, 300, 50, 20))

    
   
    canvas.blit(nyancat, (cat_x, cat_y))

    
    if game_over:
        font = pygame.font.SysFont(None, 40)
        text = font.render("Game Over! Press R", True, (255, 255, 255))
        canvas.blit(text, (100, 200))
=======
    
    world_x -= speed

    canvas.fill(color)

   
    for i in range(0, 1000, 100):
        pygame.draw.rect(canvas, (255, 255, 255), (i + world_x, 300, 50, 20))

   
    canvas.blit(nyancat, (cat_x, cat_y))
>>>>>>> d8a5a44167dcf42a4598f7809b16e32e197dc5d9

    pygame.display.update()

pygame.quit()