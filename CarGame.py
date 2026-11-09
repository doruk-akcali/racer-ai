"""Playable version of the game: drive the car around the track with the arrow keys."""

import pygame
from Car import Car
from Track import Track


def draw_hud(screen, font, car, track):
    """Draw the lap, checkpoint and lap-time text in the top-left corner.

    It only reads the car's state, so the game logic works without it.

    Args:
        screen: The surface to draw on.
        font: The pygame Font, created once before the game loop.
        car: The Car whose progress is shown.
        track: The Track, for the number of checkpoints.
    """
    seconds = car.lap_frames / 60
    best = "--" if car.best_lap_frames is None else f"{car.best_lap_frames / 60:.1f} s"

    line1 = (f"Lap {car.lap + 1}   CP {car.next_checkpoint}/{len(track.checkpoints)}   "
             f"{seconds:.1f} s")
    line2 = f"Best lap: {best}"

    text1 = font.render(line1, True, (255, 255, 255), (0, 0, 0))  # Black background keeps the text readable anywhere on the track
    text2 = font.render(line2, True, (255, 255, 255), (0, 0, 0))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))


pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True

track = Track()
car = Car(**track.start)  # Unpacks {"x", "y", "angle"} into Car(x=..., y=..., angle=...)
font = pygame.font.Font(None, 30)   # None = pygame's built-in font

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
    draw_hud(screen, font, car, track)
    pygame.display.flip()    
    clock.tick(60)  # The physics is per frame, so the frame rate sets the game speed
pygame.quit()