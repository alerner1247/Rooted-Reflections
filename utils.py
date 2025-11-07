
import pygame

def write(surface: pygame.Surface, text: str, color: pygame.Color, fontsize: int, x: float, y: float) -> pygame.Surface:
    text_surface = pygame.font.SysFont("Brush Script MT", fontsize).render(text, True, color)
    surface.blit(text_surface, (x, y))

