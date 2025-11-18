import pygame
pygame.init()

class MusicButton():

    def __init__(self, screen: pygame.Surface, x, y, w, h):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.white = (255,255,255)
        self.pink = (255, 150, 190)

        #button basic setup
        self.button_rect = pygame.Rect(self.x, self.y, self.w, self.h)  # x, y, width, height
        self.font = pygame.font.Font(None, 40)


        pygame.mixer.music.load("/Users/priscillalu/Downloads/lofi.mp3")

    def music_running(self):
            pygame.draw.rect(self.screen, self.pink, self.button_rect, border_radius = 10)

            # draw text
            text = self.font.render("Play Music", True, self.white)
            text_rect = text.get_rect(center=self.button_rect.center)
            self.screen.blit(text, text_rect)

    
    def point_inside(self, x: float, y: float) -> bool:
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True
        else:
            return False

