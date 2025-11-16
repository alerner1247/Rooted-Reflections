import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Rooted Reflections")

font = pygame.font.SysFont("Arial", 18)
small_font = pygame.font.SysFont("Arial", 14)
clock = pygame.time.Clock()
stored_text = ""
#Textbox class



class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = ""
        self.active = False
        self.color_inactive = (230, 230, 230)
        self.color_active = (255, 255, 255)
        self.color = self.color_inactive
    

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active when clicked
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        txt_surface = small_font.render(self.text, True, (0, 0, 0))
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))

def main():
    # Input boxes
    rose_box = InputBox(150, 80, 250, 30)
    bud_box = InputBox(150, 130, 250, 30)
    thorn_box = InputBox(150, 180, 250, 30)
    mood_box = InputBox(150, 230, 250, 30)

    # Main Loop
    running = True
    while running:
        screen.fill((248, 180, 180))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            rose_box.handle_event(event)
            bud_box.handle_event(event)
            thorn_box.handle_event(event)
            mood_box.handle_event(event)

        #Title
        title_font = pygame.font.SysFont("Arial", 28, bold=True)
        title_text = title_font.render("Reflect on your day:", True, (0, 0, 0))
        screen.blit(title_text, (130, 30))


        # Labels
        screen.blit(font.render("Rose:", True, (0, 0, 0)), (80, 85))
        screen.blit(font.render("Bud:", True, (0, 0, 0)), (80, 135))
        screen.blit(font.render("Thorn:", True, (0, 0, 0)), (80, 185))
        screen.blit(font.render("Mood: ", True, (0, 0, 0)), (80, 235))
        screen.blit(font.render("(enter either happy, sad, angered, worried,", True, (0, 0, 0)), (80, 260))
        screen.blit(font.render("excited, calm, annoyed, nervous, bored)", True, (0, 0, 0)), (80, 285))


        # Draw boxes
        rose_box.draw(screen)
        bud_box.draw(screen)
        thorn_box.draw(screen)
        mood_box.draw(screen)
    
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()