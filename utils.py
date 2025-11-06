
import pygame


def write(surface: pygame.Surface, text: str, color: pygame.Color, x: float, y: float) -> pygame.Surface:
    text_surface = pygame.font.SysFont("Arial", 30).render(text, True, color)
    surface.blit(text_surface, (x, y))

