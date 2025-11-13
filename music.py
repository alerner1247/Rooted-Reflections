import pygame
import sys

pygame.init()
pygame.mixer.init()

# Load and start music
pygame.mixer.music.load("lofi.mp3")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

    pygame.display.flip()
