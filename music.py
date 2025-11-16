import pygame
pygame.init()

# screen setup
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Button Music Player")


white = (255,255,255)
pink = (255, 150, 190)

#button basic setup
button_rect = pygame.Rect(175, 150, 150, 60)  # x, y, width, height
font = pygame.font.Font(None, 40)


pygame.mixer.music.load("/Users/priscillalu/Downloads/lofi.mp3")

running = True
while running:
    screen.fill(white)

    # daw button
    pygame.draw.rect(screen, pink, button_rect, border_radius = 10)

    # draw text
    text = font.render("Play Music", True, white)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                pygame.mixer.music.play()   #start music!!!

    pygame.display.flip()

pygame.quit()

