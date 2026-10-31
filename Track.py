"""Track image, collision layer and track data, loaded from assets/."""

import pygame
import json
from pathlib import Path

class Track:
    """The race track: what is drawn, what the car can hit, and where it starts.

    The visible image and the collision layer are separate files, so the
    track can be decorated without the decorations becoming walls.
    """

    assets = Path(__file__).parent / "assets"  # Relative to this file, so the game runs from any folder

    def __init__(self):
        """Load the track image, the wall mask and track.json."""
        self.track_image = pygame.image.load(self.assets / "track.png").convert()  # No transparency needed, and convert() makes blitting fast
        self.track_walls = pygame.image.load(self.assets / "track_walls.png").convert_alpha()
        self.json_data = json.loads((self.assets / "track.json").read_text())
        self.track_mask = pygame.mask.from_surface(self.track_walls)  # Walls are the opaque pixels
        self.start = self.json_data["start"]  # {"x", "y", "angle"}, ready for Car(**track.start)

    def draw(self, screen):
        """Draw the track; it covers the whole screen, so it also erases the last frame."""
        screen.blit(self.track_image, (0, 0))

    def collides(self, mask, rect):
        """Return True if the mask touches a wall.

        Args:
            mask: Collision mask of the object, e.g. from Car.get_mask().
            rect: Where that mask sits on the screen.
        """
        # The offset is the position of mask's top-left corner inside the track mask
        return self.track_mask.overlap(mask, (rect.x, rect.y)) is not None
       
    