import pygame

pygame.init()

screen = pygame.display.set_mode([1000, 500])
running = True
rocket = pygame.image.load('rocket.png')
rocket_x_iv = 32
rocket_y_iv = 70
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(rocket,(500-rocket_x_iv,500-rocket_y_iv))
    pygame.display.update()

pygame.quit()
