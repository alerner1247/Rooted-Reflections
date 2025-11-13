import sys
import pygame
import pygame.locals
from utils import write
from button import Button
from garden import Flower

pygame.init()


def draw(screen: pygame.Surface, button1: Button):
    write(screen, "Welcome!", (255, 255, 255), 50, 100, 100)
    button1.update()


def draw_directory(screen: pygame.Surface, button2: Button, button3: Button):
    screen.fill("#fcb7b7")
    write(screen, "directory", (0, 0, 0), 50, 150, 100)
    button2.update()
    button3.update()


def draw_graden(screen: pygame.Surface, Flowers:list):
    screen.fill("#000000")
    for flower in Flowers:
        if input_1 == sad:
            flower.update.sad
        if input_1 == 


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    button1 = Button("let's get started", screen, (255, 200, 255), 100, 250)
    button2 = Button("your garden", screen, (200, 200, 200), 50, 250)
    button3 = Button("rose, bud, thorn", screen, (0, 0, 0), 250, 250)
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
                    if button2.point_inside(x, y):
                        state = 2
                elif state == 1:
                    if button3.point_inside(x, y):
                        state = 3

        if state == 0:
            draw(screen, button1)
        if state == 1:
            draw_directory(screen, button2, button3)
        if state == 2:
            ...
        if state == 3:
            ...

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
