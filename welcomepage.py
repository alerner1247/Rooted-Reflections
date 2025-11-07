import sys
import pygame
import pygame.locals
pygame.init()
font_1 = pygame.font.SysFont("Arial", 30)

def write(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))

def draw(screen: pygame.Surface):
    screen.fill("#FFC8C8")

class button():
    0

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()


        draw(screen)
        write(screen, "welcome", font_1, (255,255,255), 100, 100)
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()