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

def draw_garden(screen, flower1: Flower):
    screen.fill("#ffffff")
    flower1.update()
    """flower2.update()
    flower3.update()
    flower4.update()
    flower5.update()
    flower6.update()
    flower7.update(), flower2: Flower, flower3: Flower, flower4: Flower, flower5: Flower, flower6: Flower, flower7: Flower"""

def draw_info(screen):
    screen.fill("#000000")
    if os.path.exists("stored_text.pkl"):
        with open("stored_text.pkl", "rb") as f:
            data = pickle.load(f)
    else:
        data = []
    if len(data) > 7:
        data = data[-6:]
    text = input()
    data.append(text)
    print(data)
    with open("stored_text.pkl", "wb") as f:
        pickle.dump(data, f)
    
    write(screen, data, "#ffffff", 20, 100, 100)

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
    rose_box_inputs = []
    bud_box_inputs = []
    thorn_box_inputs = []
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
                    if flower1.point_inside(x, y):
                        state = 4
            if state == 2:
                rose_box.handle_event(event)
                bud_box.handle_event(event)
                thorn_box.handle_event(event)
                mood_box.handle_event(event)
                if submit_button.point_inside(x, y):
                    rose_box_inputs.append(rose_box.text)
                    bud_box_inputs.append(bud_box.text)
                    thorn_box_inputs.append(thorn_box_inputs)
                    if mood_box.text in emotion_colors:
                        flower1 = Flower(30, 30, screen, emotion_colors[mood_box.text], 100, 100)
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
            if os.path.exists("stored_text.pkl"):
                with open("stored_text.pkl", "rb") as f:
                    data = pickle.load(f)
            else:
                data = []
            if len(data) > 7:
                data = data[-6:]
            text = input(rose_box_inputs)
            data.append(text)
            print(data)
            with open("stored_text.pkl", "wb") as f:
                pickle.dump(data, f)
    


        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
