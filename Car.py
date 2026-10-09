class Car: 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 0
        self.angle = 0

    def movement(self):
        # Update position based on speed and angle
        self.x += self.speed * pygame.math.cos(pygame.math.radians(self.angle))
        self.y -= self.speed * pygame.math.sin(pygame.math.radians(self.angle))

    def draw(self, screen):
        # Draw the car as a rectangle for simplicity
        car_rect = pygame.Rect(self.x, self.y, 50, 30)
        pygame.draw.rect(screen, self.color, car_rect)