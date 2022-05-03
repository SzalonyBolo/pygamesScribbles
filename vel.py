import pygame

pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

x, y, width, height = 50, 50, 40, 60
vel = 5

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_LEFT]:
        x -= vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 

pygame.quit() 