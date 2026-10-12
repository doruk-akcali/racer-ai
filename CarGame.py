import pygame
from Car import Car
from Track import Track

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

track = Track()
car = Car(track.start["x"], track.start["y"], track.start["angle"])  # create a car instance

while running:
    
    # handle events   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        car.accelerate(0.5)
    if pressed[pygame.K_DOWN]:
        car.brake(0.5)
    if pressed[pygame.K_LEFT]:
        car.turn(-5)
    if pressed[pygame.K_RIGHT]:
        car.turn(5)
        
    # 2. update game state here
    car.move()
    track.draw(screen)
    car.draw(screen)
    pygame.display.flip()                 # show the frame
    clock.tick(60)                        # cap at 60 FPS

pygame.quit()