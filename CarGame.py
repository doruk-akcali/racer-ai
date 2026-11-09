"""Playable version of the game: drive the car around the track with the arrow keys."""

import pygame
from Car import Car
from Track import Track

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

track = Track()
car = Car(**track.start)  # Unpacks {"x", "y", "angle"} into Car(x=..., y=..., angle=...)

while running:
    
    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Input: polled every frame, so holding a key keeps acting
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        car.accelerate()
    if pressed[pygame.K_DOWN]:
        car.brake()
    if pressed[pygame.K_LEFT]:
        car.turn(-1)
    if pressed[pygame.K_RIGHT]:
        car.turn(1)
        
    # 3. Update and draw
    car.move()
    track.draw(screen)
    

    car_mask, car_rect = car.get_mask()
    if track.collides(car_mask, car_rect):
        car.reset(**track.start)  # Crash: back to the start
    else:
        car.update_progress(track, car_rect)
    car.draw(screen)  # After the track, so the car is drawn on top
    pygame.display.flip()    
    clock.tick(60)  # The physics is per frame, so the frame rate sets the game speed
pygame.quit()