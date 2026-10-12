import pygame
import json
from pathlib import Path

class Track:

    assets = Path(__file__).parent / "assets"

    def __init__(self):
        self.track_image = pygame.image.load(self.assets / "track.png").convert()
        self.track_walls = pygame.image.load(self.assets / "track_walls.png").convert_alpha()
        self.json_data = json.loads((self.assets / "track.json").read_text())
        self.track_mask = pygame.mask.from_surface(self.track_walls)
        self.start = self.json_data["start"]

    def draw(self, screen):
        screen.blit(self.track_image, (0, 0))
    