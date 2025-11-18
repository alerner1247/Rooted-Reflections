import pygame
pygame.init()

class MusicButton():

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.white = (255,255,255)
        self.pink = (255, 150, 190)

        #button basic setup
        self.button_rect = pygame.Rect(175, 150, 150, 60)  # x, y, width, height
        self.font = pygame.font.Font(None, 40)


        # pygame.mixer.music.load("lofi.mp3")

    def music_running(self):
        running = True
        while running:

            pygame.draw.rect(self.screen, self.pink, self.button_rect, border_radius = 10)

            # draw text
            text = self.font.render("Play Music", True, self.white)
            text_rect = text.get_rect(center=self.button_rect.center)
            self.screen.blit(text, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    pygame.mixer.music.play()   #start music!!!

