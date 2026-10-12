from pathlib import Path
import pygame
import math

class Car: 

    MAX_SPEED = 7 
    FRAMES_TO_TOP = 90
    FRICTION = 0.05 **(1/FRAMES_TO_TOP)  # Friction factor to reduce speed over time
    ACCELERATION = MAX_SPEED * (1 - FRICTION) / FRICTION  # Acceleration factor to reach max speed in FRAMES_TO_TOP frames
    BRAKING = 0.3
    TURN_PER_SPEED = 0.6
    MAX_TURN = 3

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y 
        self.speed = 0
        self.angle = angle 
        self.image = pygame.image.load(Path(__file__).parent / "assets" / "car.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 30))  # Scale the car image to a smaller size

    def move(self):
        # Update position based on speed
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.speed *= self.FRICTION  # Apply friction to gradually slow down the car
        if self.speed < 0.001 and self.speed > -0.001:
            self.speed = 0  # Stop the car if speed is very low
        
    def draw(self, screen):
        # Draw the car as a custom image rotated based on the angle
        rotated_image, rect = self.rotated()
        screen.blit(rotated_image, rect.topleft)
        
    def rotated(self):
        rotated = pygame.transform.rotate(self.image, -self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        return rotated, rect
    
    def get_mask(self):
        rotated_image, rect = self.rotated()
        return pygame.mask.from_surface(rotated_image), rect
    
    def accelerate(self):
        self.speed += self.ACCELERATION

    def brake(self):
        self.speed -= self.BRAKING

    def turn(self, direction):
        delta_angle = direction * min(self.TURN_PER_SPEED * abs(self.speed), self.MAX_TURN)
        if self.speed > 0:
            self.angle += delta_angle
        else: 
            self.angle -= delta_angle

    def reset(self, x, y, angle):
        # Reset the car's position and angle
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0  # Reset speed to 0 when resetting the car



    