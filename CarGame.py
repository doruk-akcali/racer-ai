import pygame
from Car import Car
from Track import Track

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

track = Track()
car = Car(**track.start)  # create a car instance

while running:
    
    # handle events   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        car.accelerate()
    if pressed[pygame.K_DOWN]:
        car.brake()
    if pressed[pygame.K_LEFT]:
        car.turn(-1)
    if pressed[pygame.K_RIGHT]:
        car.turn(1)
        
    # 2. update game state here
    car.move()
    track.draw(screen)
    

    car_mask, car_rect = car.get_mask()  # get the car's collision mask
    if track.collides(car_mask, car_rect):
        car.reset(**track.start)  # reset the car to the starting position and angle

    car.draw(screen)
    pygame.display.flip()    
    clock.tick(60)          
pygame.quit()