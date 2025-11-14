import sys
import pygame
import pygame.locals
from utils import write
from button import Button
from data_input import InputBox

pygame.init()

def draw(screen: pygame.Surface, button1: Button):
    write(screen, "Welcome!", (255, 255, 255), 50, 100, 100)
    button1.update()


def draw_directory(screen: pygame.Surface, button2: Button, button3: Button):
    screen.fill("#fcb7b7")
    write(screen, "directory", (0, 0, 0), 50, 150, 100)
    button2.update()
    button3.update()

def draw_input(screen: pygame.Surface, rose_box: InputBox, bud_box: InputBox, thorn_box: InputBox, mood_box: InputBox):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")

    font = pygame.font.SysFont("Arial", 18)
    small_font = pygame.font.SysFont("Arial", 14)
    
    title_font = pygame.font.SysFont("Arial", 28, bold=True)
    title_text = title_font.render("Reflect on your day:", True, (0, 0, 0))
    screen.blit(title_text, (130, 30))

    screen.blit(font.render("Rose:", True, (0, 0, 0)), (80, 85))
    screen.blit(font.render("Bud:", True, (0, 0, 0)), (80, 135))
    screen.blit(font.render("Thorn:", True, (0, 0, 0)), (80, 185))
    screen.blit(font.render("Mood: ", True, (0, 0, 0)), (80, 235))
    screen.blit(font.render("(enter either happy, sad, angered, worried,", True, (0, 0, 0)), (80, 260))
    screen.blit(font.render("overstimulated, excited,", True, (0, 0, 0)), (80, 285))
    screen.blit(font.render("calm, annoyed, nervous, bored)", True, (0, 0, 0)), (80, 310))


    rose_box.draw(screen)
    bud_box.draw(screen)
    thorn_box.draw(screen)
    mood_box.draw(screen)

def main():
    print("yo")
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    button1 = Button("let's get started", screen, (255, 200, 255), 100, 250)
    button2 = Button("your garden", screen, (200, 200, 200), 50, 250)
    button3 = Button("rose, bud, thorn", screen, (0, 0, 0), 250, 250)
    state = 0
    rose_box = InputBox(150, 80, 250, 30)
    bud_box = InputBox(150, 130, 250, 30)
    thorn_box = InputBox(150, 180, 250, 30)
    mood_box = InputBox(150, 230, 250, 30)


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
                        state = 3
                    if button3.point_inside(x, y):
                        state = 2
                elif state == 2:
                    rose_box.handle_event(event)
                    bud_box.handle_event(event)
                    thorn_box.handle_event(event)
                    mood_box.handle_event(event)

        if state == 0:
            draw(screen, button1)
        elif state == 1:
            draw_directory(screen, button2, button3)
        elif state == 2:
            draw_input(screen, rose_box, bud_box, thorn_box, mood_box)
        elif state == 3:
            ...

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
