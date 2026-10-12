from pathlib import Path
import pygame
import math

class Car: 

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
        self.speed *= 0.95  # Apply friction to gradually slow down the car
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
        rotated_image, _ = self.rotated()
        return pygame.mask.from_surface(rotated_image)
    
    def accelerate(self, amount):
        # Increase speed in the direction of the angle
        self.speed += amount

    def brake(self, amount):
        # Decrease speed in the direction of the angle
        self.speed -= amount

    def turn(self, angle_change):
        # Change the angle of the car
        angle_change = angle_change * self.speed / 10  # Adjust turning based on speed
        self.angle += angle_change
        self.angle %= 360  # Keep the angle within 0-359 degrees

    def reset(self, x, y, angle):
        # Reset the car's position and angle
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0  # Reset speed to 0 when resetting the car



    