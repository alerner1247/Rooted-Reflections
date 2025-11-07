import sys

import pygame as pg
import pygame.locals


bg_color = "#FAC2C2"
text_color = pg.Color("black")
box_color = pg.Color("white")
highlight = pg.Color("#F9C4C4")
font = pg.font.Font(None, 32)



class Textbox:
    def __init__(self, x, y, w, h, label):
        self.rect = pg.Rect(x, y, w, h)
        self.color = box_color
        self.text = ""
        self.txt_surface = font.render(self.text, True, text_color)
        self.active = False
        self.label = font.render(label, True, text_color)
        
    def draw(screen: pygame.Surface):
        screen.fill("#F8B4B4")



def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    


    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        draw(screen)

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()