import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():      # 1. handle events
        if event.type == pygame.QUIT:
            running = False

    # 2. update game state here

    screen.fill((30, 30, 30))             # 3. draw
    # draw track, car...
    pygame.display.flip()                 # show the frame

    clock.tick(60)                        # cap at 60 FPS

pygame.quit()