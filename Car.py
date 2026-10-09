from pathlib import Path
import pygame
import math

class Car: 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 0
        self.angle = 0
        self.image = pygame.image.load(Path(__file__).parent / "assets" / "car.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 30))  # Scale the car image to a smaller size

    def move(self):
        # Update position based on speed
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.speed *= 0.95  # Apply friction to gradually slow down the car
        if self.speed < 0.001 and self.speed > -0.001:
            self.speed = 0  # Stop the car if speed is very low
        self.x = max(0, min(self.x, 1200))  # Keep the car within the screen bounds
        self.y = max(0, min(self.y, 800))   # Keep the car within the screen bounds
        
    def draw(self, screen):
        # Draw the car as a rectangle for simplicity
        rotated = pygame.transform.rotate(self.image, -self.angle)  # Rotate the car image based on the angle
        screen.blit(rotated, rotated.get_rect(center=(self.x, self.y)))
        

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



    