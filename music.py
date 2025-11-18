import pygame
pygame.init()

class MusicButton():

    def __init__(self):
    # screen setup
        self.width, self.height = 500, 400
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("Button Music Player")
        self.white = (255,255,255)
        self.pink = (255, 150, 190)

        #button basic setup
        self.button_rect = pygame.Rect(175, 150, 150, 60)  # x, y, width, height
        self.font = pygame.font.Font(None, 40)


        # pygame.mixer.music.load("/Users/priscillalu/Downloads/lofi.mp3")

    def music_running(self):
        running = True
        while running:
            self.screen.fill(self.white)

            # daw button
            pygame.draw.rect(self.screen, self.pink, self.button_rect, border_radius = 10)

            # draw text
            text = self.font.render("Play Music", True, self.white)
            text_rect = text.get_rect(center=self.button_rect.center)
            self.screen.blit(text, text_rect)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # check mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        pygame.mixer.music.play()   #start music!!!
            pygame.display.flip()

pygame.quit()

