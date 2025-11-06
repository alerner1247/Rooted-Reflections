import pygame
from utils import write


class Button:
    def __init__(
        self, text: str, screen: pygame.Surface, color: pygame.Color, x: float, y: float
    ):
        self.x = x
        self.y = y
        self.w = 150
        self.h = 70
        self.color = color
        self.surface = screen
        self.text = text

    def update(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.w, self.h))
        write(self.surface, self.text, (24, 78, 0), self.x, self.y)

    def point_inside(self, x: float, y: float) -> bool:
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True
        else:
            return False
