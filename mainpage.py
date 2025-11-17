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


def draw_directory(screen: pygame.Surface, button2: Button, button3: Button):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")
    write(screen, "directory", (0, 0, 0), 50, 150, 100)
    button2.update()
    button3.update()

def draw_input(screen: pygame.Surface, rose_box: InputBox, bud_box: InputBox, thorn_box: InputBox, mood_box: InputBox, submit_button: Button):
    screen.fill("#fcb7b7")
    pygame.display.set_caption("Rooted Reflections")

    font = pygame.font.SysFont("Arial", 18)
    
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

    submit_button.update()
    rose_box.draw(screen)
    bud_box.draw(screen)
    thorn_box.draw(screen)
    mood_box.draw(screen)

def draw_garden(screen, Flowers: list):
    screen.fill("#ffffff")
    for flower in Flowers:
        flower.update
    

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 500, 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    button1 = Button("let's get started", screen, (255, 255, 255), 100, 250)
    button2 = Button("your garden", screen, (200, 200, 200), 30, 250)
    button3 = Button("rose, bud, thorn", screen, "#ffffff", 280, 250)
    state = 0
    rose_box = InputBox(150, 80, 250, 30)
    bud_box = InputBox(150, 130, 250, 30)
    thorn_box = InputBox(150, 180, 250, 30)
    mood_box = InputBox(150, 230, 250, 30)
    submit_button = Button("submit", screen, (255, 255, 255), 250, 400)
    emotion_colors = {"happy": "#F88379", "sad": "#0047AB", "angered": "#8B0000", "excited": "#FFEA00", "calm":"#6F8FAF", "annoyed":"#AA4A44", "nervous": "#AFE1AF", "bored":"#B2BEB5"}
    flower1 = None

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
                elif state == 3:
                    if flower.point_inside(x, y):
                        state = 4
                        if os.path.exists("stored_rose_box_text.pkl"):
                            with open("stored_rose_box_text.pkl", "rb") as f:
                                data1 = pickle.load(f)
                        else:
                            data1 = []
                        if len(data1) > 7:
                            data1 = data1[-6:]
                        data1.append(rose_box.text)
                        print(data1[0])
                        with open("stored_rose_box_text.pkl", "wb") as f:
                            pickle.dump(data1, f)

                        if os.path.exists("stored_bud_box_text.pkl"):
                            with open("stored_bud_box_text.pkl", "rb") as f:
                                data2 = pickle.load(f)
                        else:
                            data2 = []
                        if len(data2) > 7:
                            data2 = data2[-6:]
                        data2.append(bud_box.text)
                        print(data2[0])
                        with open("stored_bud_box_text.pkl", "wb") as f:
                            pickle.dump(data2, f)
                        
                        if os.path.exists("stored_thorn_box_text.pkl"):
                            with open("stored_thorn_box_text.pkl", "rb") as f:
                                data3 = pickle.load(f)
                        else:
                            data3 = []
                        if len(data3) > 7:
                            data3 = data3[-6:]
                        data3.append(thorn_box.text)
                        print(data3[0])
                        with open("stored_thorn_box_text.pkl", "wb") as f:
                            pickle.dump(data3, f)
                        
                        if os.path.exists("stored_mood_box_text.pkl"):
                            with open("stored_mood_box_text.pkl", "rb") as f:
                                data4 = pickle.load(f)
                        else:
                            data4 = []
                        if len(data4) > 7:
                            data4 = data4[-6:]
                        data4.append(thorn_box.text)
                        print(data4[0])
                        with open("stored_mood_box_text.pkl", "wb") as f:
                            pickle.dump(data4, f)
                        
            if state == 2:
                rose_box.handle_event(event)
                bud_box.handle_event(event)
                thorn_box.handle_event(event)
                mood_box.handle_event(event)
                if submit_button.point_inside(x, y):
                    if mood_box.text in emotion_colors:
                        flower in Flowers = Flower(30, 30, screen, emotion_colors[mood_box.text], 100, 100)
                    state = 3
            
                
                
        if state == 0:
            draw(screen, button1)
        elif state == 1:
            draw_directory(screen, button2, button3)
        elif state == 2:
            draw_input(screen, rose_box, bud_box, thorn_box, mood_box, submit_button)
        elif state == 3:
            draw_garden(screen, flower1)
        elif state == 4:
            screen.fill("#000000")
    


        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
