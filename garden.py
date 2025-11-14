import sys
import math
import pygame
import pygame.locals


pygame.init()

class Flower:
    def __init__(
        self,
        r_petal: float,
        r_center: float,
        screen: pygame.Surface,
        color: pygame.Color,
        x: float,
        y: float,
    ):
        self.surface = screen
        self.color = color
        self.x = x
        self.y = y
        self.r_petal = r_petal
        self.r_center = r_center

    def update(self):
        for i in range(6):
            degrees = i * 360/6
            radians = math.radians(degrees)
            x = self.r_center * math.cos(radians) + self.x
            y = self.r_center * math.sin(radians) + self.y
            pygame.draw.circle(
                self.surface,
                self.color,
                (x, y),
                self.r_petal,
            )
        pygame.draw.circle(self.surface, "#FFFF8F", (self.x, self.y), self.r_center)

    def sad(self):
        self.color = "#6495ED"
    def happy(self):
        self.color = "#F88379"
    def angry(self):
        self.color = "#FF0000"
    
    def point_inside(self, x: float, y: float) -> bool:
        if self.x < x < self.x + self.r_center + self.r_petal and self.y < y < self.r_center + self.r_petal:
            return True
        else:
            return False
def Color():
    if 
def draw(screen: pygame.Surface, flower_1: Flower):
    screen.fill("#000000")
    flower_1.update()

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    flower_1 = Flower(30, 30, screen, color=Color, 100, 100)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        draw(screen, flower_1)

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
