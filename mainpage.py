import sys
import pygame
import pygame.locals
from utils import write
from button import Button
from data_input import InputBox
from garden import Flower
import pickle
import os 

pygame.init()

def draw(screen: pygame.Surface, button1: Button):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")
    write(screen, "Welcome!", (255, 255, 255), 50, 100, 100)
    button1.update()


def draw_directory(screen: pygame.Surface, button2: Button, button3: Button, mbutton: MusicButton):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")
    write(screen, "directory", (0, 0, 0), 50, 150, 100)
    button2.update()
    button3.update()
    mbutton.music_running()


def draw_input(screen: pygame.Surface, rose_box: InputBox, bud_box: InputBox, thorn_box: InputBox, mood_box: InputBox, submit_button: Button):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")

    font = pygame.font.Font("Vanilla Pancake.ttf", 18)
    
    title_font = pygame.font.Font("Vanilla Pancake.ttf", 28, bold=True)
    title_text = title_font.render("Reflect on your day:", True, (0, 0, 0))
    screen.blit(title_text, (130, 30))

    screen.blit(font.render("Rose:", True, (0, 0, 0)), (80, 85))
    screen.blit(font.render("Bud:", True, (0, 0, 0)), (80, 135))
    screen.blit(font.render("Thorn:", True, (0, 0, 0)), (80, 185))
    screen.blit(font.render("Mood: ", True, (0, 0, 0)), (80, 235))
    screen.blit(font.render("(enter either happy, sad, angered, worried,", True, (0, 0, 0)), (80, 260))
    screen.blit(font.render("overstimulated, excited,", True, (0, 0, 0)), (80, 285))
    screen.blit(font.render("calm, annoyed, nervous, bored)", True, (0, 0, 0)), (80, 310))

    submit_button.update()
    rose_box.draw(screen)
    bud_box.draw(screen)
    thorn_box.draw(screen)
    mood_box.draw(screen)

def draw_garden(screen, flowers: list[Flower]):
    screen.fill("#ffffff")
    for flower in flowers:
        flower.update()
    

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    button1 = Button("let's get started", screen, (255, 255, 255), 100, 250)
    button2 = Button("your garden", screen, (200, 200, 200), 30, 250)
    button3 = Button("rose, bud, thorn", screen, "#ffffff", 280, 250)
    mbutton = MusicButton(screen)
    state = 0
    rose_box = InputBox(150, 80, 250, 30)
    bud_box = InputBox(150, 130, 250, 30)
    thorn_box = InputBox(150, 180, 250, 30)
    mood_box = InputBox(150, 230, 250, 30)
    submit_button = Button("submit", screen, (255, 255, 255), 250, 400)
    emotion_colors = {"happy": "#F88379", "sad": "#0047AB", "angered": "#8B0000", "excited": "#FFEA00", "calm":"#6F8FAF", "annoyed":"#AA4A44", "nervous": "#AFE1AF", "bored":"#B2BEB5"}
    
    flowers = []
    if os.path.exists("stored_rose_box_text.pkl"):
        with open("stored_rose_box_text.pkl", "rb") as f:
            rose_data = pickle.load(f)
    else:
        rose_data = []
    if len(rose_data) > 7:
        rose_data = rose_data[-6:]

    if os.path.exists("stored_bud_box_text.pkl"):
        with open("stored_bud_box_text.pkl", "rb") as f:
            bud_data = pickle.load(f)
    else:
        bud_data = []
    if len(bud_data) > 7:
        bud_data = bud_data[-6:]

    if os.path.exists("stored_thorn_box_text.pkl"):
        with open("stored_thorn_box_text.pkl", "rb") as f:
            thorn_data = pickle.load(f)
    else:
        thorn_data = []
    if len(thorn_data) > 7:
        thorn_data = thorn_data[-6:]

    if os.path.exists("stored_mood_box_text.pkl"):
        with open("stored_mood_box_text.pkl", "rb") as f:
            mood_data = pickle.load(f)
    else:
        mood_data = []
    if len(mood_data) > 7:
        mood_data = mood_data[-6:]

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
                # elif state == 3:
                #     if flower.point_inside(x, y):
                #         state = 4
                        
            if state == 2:
                rose_box.handle_event(event)
                bud_box.handle_event(event)
                thorn_box.handle_event(event)
                mood_box.handle_event(event)
                if submit_button.point_inside(x, y) and mood_box.text in emotion_colors:
                    rose_data.append(rose_box.text)
                    with open("stored_rose_box_text.pkl", "wb") as f:
                        pickle.dump(rose_data, f)

                    bud_data.append(bud_box.text)
                    with open("stored_bud_box_text.pkl", "wb") as f:
                        pickle.dump(bud_data, f)
                    
                    thorn_data.append(thorn_box.text)
                    with open("stored_thorn_box_text.pkl", "wb") as f:
                        pickle.dump(thorn_data, f)
                    
                    mood_data.append(mood_box.text)
                    with open("stored_mood_box_text.pkl", "wb") as f:
                        pickle.dump(mood_data, f)
                    for i in range(len(mood_data)):
                        color = emotion_colors[mood_data[i]]
                        f = Flower(30, 30, screen, color, i*20, 50)
                        flowers.append(f)
                    
                    state = 3
            
                
                
        if state == 0:
            draw(screen, button1)
        elif state == 1:
            draw_directory(screen, button2, button3, mbutton)
        elif state == 2:
            draw_input(screen, rose_box, bud_box, thorn_box, mood_box, submit_button, mbutton)
        elif state == 3:
            draw_garden(screen, flowers)
        elif state == 4:
            screen.fill("#000000")
    


        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
