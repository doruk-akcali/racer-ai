"""Car physics and rendering for the racing game."""

from pathlib import Path
import pygame
import math

class Car: 
    """A top-down car driven by a speed and a heading angle.

    The angle is in degrees: 0 faces right, and it grows clockwise on screen
    because pygame's y axis points down. Physics constants are class
    attributes, so every car shares them.
    """

    MAX_SPEED = 7  # Top speed in pixels per frame
    FRAMES_TO_TOP = 90  # Frames to reach 95% of top speed (1.5 s at 60 FPS)
    FRICTION = 0.05 **(1/FRAMES_TO_TOP)  # Speed kept per frame; only 5% of the gap to top speed is left after FRAMES_TO_TOP frames
    ACCELERATION = MAX_SPEED * (1 - FRICTION) / FRICTION  # Chosen so friction cancels it exactly at MAX_SPEED
    BRAKING = 0.3  # Speed removed per frame while braking
    TURN_PER_SPEED = 0.6  # Degrees turned per frame for each pixel/frame of speed
    MAX_TURN = 3  # Turn-rate cap in degrees per frame, reached at speed 5

    def __init__(self, x, y, angle):
        """Place a standing car at (x, y), facing angle.

        Args:
            x: Horizontal position of the car's centre, in pixels.
            y: Vertical position of the car's centre, in pixels.
            angle: Heading in degrees; 0 faces right.
        """
        self.x = x
        self.y = y 
        self.speed = 0
        self.angle = angle 
        self.image = pygame.image.load(Path(__file__).parent / "assets" / "car.png").convert_alpha()  # Keep the transparent background around the car
        self.image = pygame.transform.smoothscale(self.image, (50, 30))  # car.png is 100x60; draw it at half size

    def move(self):
        """Advance one frame: move along the heading, then apply friction."""
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y += self.speed * math.sin(math.radians(self.angle))
        self.speed *= self.FRICTION
        if self.speed < 0.001 and self.speed > -0.001:
            self.speed = 0  # Friction alone never reaches exactly 0, so snap tiny speeds
        
    def draw(self, screen):
        """Draw the car onto screen, rotated to its heading."""
        rotated_image, rect = self.rotated()
        screen.blit(rotated_image, rect.topleft)
        
    def rotated(self):
        """Return the rotated image and its rect, centred on the car.

        Rotating changes the image size, so the rect is rebuilt around the
        car's centre each time; otherwise the car would wobble while turning.
        """
        rotated = pygame.transform.rotate(self.image, -self.angle)  # pygame rotates counter-clockwise, our angle grows clockwise
        rect = rotated.get_rect(center=(self.x, self.y))
        return rotated, rect
    
    def get_mask(self):
        """Return the collision mask and rect of the rotated car.

        Returns:
            A (mask, rect) tuple, where rect is the rotated image's
            bounding box centred on the car.
        """
        rotated_image, rect = self.rotated()
        return pygame.mask.from_surface(rotated_image), rect
    
    def accelerate(self):
        """Speed up for one frame; call it every frame the key is held."""
        self.speed += self.ACCELERATION

    def brake(self):
        """Slow down for one frame; below zero the car drives in reverse."""
        self.speed -= self.BRAKING

        # Cap the speed at MAX_SPEED in reverse, so the car doesn't go backwards faster than forwards.
        if self.speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED

    def turn(self, direction):
        """Rotate the car; the turn rate grows with speed up to MAX_TURN.

        A standing car does not turn, and steering is mirrored while
        reversing, like a real car.

        Args:
            direction: -1 to steer left, 1 to steer right.
        """
        delta_angle = direction * min(self.TURN_PER_SPEED * abs(self.speed), self.MAX_TURN)
        if self.speed > 0:
            self.angle += delta_angle
            self.angle %= 360  # Keep the angle in [0, 360) for easier debugging
        else: 
            self.angle -= delta_angle
            self.angle %= 360  # Keep the angle in [0, 360) for easier debugging

    def reset(self, x, y, angle):
        """Put the car back at (x, y), facing angle, standing still."""
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0



    