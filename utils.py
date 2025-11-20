
import pygame

def write(surface: pygame.Surface, text: str, color: pygame.Color, fontsize: int, x: float, y: float) -> pygame.Surface:
    text_surface = pygame.font.SysFont("Vanilla Pancake.ttf", fontsize).render(text, True, color)
    surface.blit(text_surface, (x, y))

