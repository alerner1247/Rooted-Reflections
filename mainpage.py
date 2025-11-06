import sys
import pygame
import pygame.locals
from utils import write
from button import Button
import data_input

pygame.init()

def draw(screen: pygame.Surface):
    screen.fill("#000000")

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    button1 = Button("get started!", screen, (255, 255, 255), 100, 250)
    state = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if state == 0:
                    if button1.point_inside(x, y):
                        state = 1
                elif state == 1:
                    ...

        draw(screen)
        if state == 0:
            write(screen, "Welcome!", (255, 255, 255), 100, 100)
            button1.update()

        if state == 1:
            data_input

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
