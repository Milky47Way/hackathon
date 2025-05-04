import pygame
import sys
import os
import openai
from PIL import Image

#для ші
openai.api_key = ('gpt:AU54YW8RRi4TXANWp060hfjiJxU6btLIvPmqxAgYF0QLgPDwmNfdLT5NyC9Y8r_u4QZeQmwhzFJFkblB3T4yhgCdA9W2KZIQwDchnwN-SRJKHph3pqraKQNsAmcDeSXdm_4aNY-8_3oiLFalGXckzNJlfA-T')

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Ти мила аніме-дівчина в отоме грі."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def play_click_sound():
    pass

#сцена, музика
width = 800
height = 600

back = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Draconic Age')
icon = pygame.image.load('Dragon.png')
pygame.display.set_icon(icon)

pygame.init()
pygame.mixer.init()

music_on = True
music_path = os.path.join(os.path.dirname(__file__), "res/Angels Airwaves - The Adventure.mp3")

white = (255, 255, 255)
black = (0,0,0)
gray = (200, 200, 200)

font = pygame.font.SysFont(None, 60)

box = pygame.Rect(50, 500, 700, 50)
color_inactive = gray
color_active = (0, 255, 0)
color = color_inactive
active = False
text = ''
chat_history = []

current_language = 'ua'

def return_to_main_menu():
    pass

def draw_chat():
    y = 50
    for msg in chat_history[-10:]:
        msg_surface = font.render(msg, True, black)
        back.blit(msg_surface, (50, y))
        y += 30

box = pygame.Rect(50, height - 80, 700, 40)  # Текстове поле
active = False
color_inactive = pygame.Color('gray')
color_active = pygame.Color('lightskyblue')
color = color_inactive
text = ''
chat_history = []  # Історія чату

def get_ai_response(user_input):
    return "he?" + text

def load_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f'none')
        return None

def display_text_from_file(file_path, start_y=320, text_size=40):
    try:
        with open(file_path, 'r', encoding= 'utf-8') as file:
            lines = file.readlines()
            font = pygame.font.SysFont(None, text_size)
            x = 10
            y = start_y
            for line in lines:
                text_surface =font.render(line.strip(), True, (255, 255, 255))
                text_rect = text_surface.get_rect(topleft=(x,y))
                back.blit(text_surface, text_rect)
                y += text_size + 10

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")

def toggle_language():
    #load_info_text()
    global current_language
    current_language = 'en' if current_language == 'ua' else 'ua'
    print("yess")


def draw_button(text, x, y, w, h, color, action):
    pygame.draw.rect(back, color, (x, y, w, h))
    button_font =  pygame.font.SysFont(None, 36)
    text_surf = button_font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    back.blit(text_surf, text_rect)
       # mouse = pygame.mouse.get_pos()

    if action:
        if pygame.mouse.get_pressed()[0]:
            if pygame.Rect(x, y, w, h).collidepoint(pygame.mouse.get_pos()):
                action()

# Функції для кнопок
def start_game():
    start_back()

def info_game():
    info_back()

def settings_game():
    settings_back()

#меню ігр
def start_back():
    while True:
        back.fill((240, 240, 240))
        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render('Start back', True, (50, 50, 50))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        back.blit(text, text_rect)
        draw_button('Menu', width // 2 - 150, height // 2 + 200, 300, 60, (100, 200, 100), return_to_main_menu)
        draw_button('Game', width // 2 - 150, height // 2 - 200, 300, 60, (100, 200, 100), start2_back)
        draw_button('Game', width // 2 - 150, height // 2 + 20, 300, 60, (100, 200, 100), start1_back)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()


#меню лабіринт
def start1_back():
    while True:
        back.fill((240, 240, 240))
        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render('Start', True, (50, 50, 50))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        back.blit(text, text_rect)
        draw_button('Menu', width // 2 - 150, height // 2 + 200, 300, 60, (100, 200, 100), return_to_main_menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()

#меню квест
def start2_back():
    global text, active, color
    while True:
        back.fill((240, 240, 240))

        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render('', True, (50, 50, 50))
        text_display = font_big.render('Chat-GPT', True, (50, 50, 50))
        text_rect = text_display.get_rect(center=(width // 2, height // 2 - 200))
        back.blit(text_display, text_rect)

        text_rect = text.get_rect(center=(width // 2, height // 2))
        back.blit(text, text_rect)
        draw_button('Menu', width // 2 - 150, height // 2 + 200, 300, 60, (100, 200, 100), return_to_main_menu)
        draw_chat()

        color = ('blue')
        pygame.draw.rect(back, color, box, 2)
        text = ''
        txt_surf = font.render(text, True, black)
        back.blit(txt_surf, (box.x + 5, box.y + 5))
        box.w = max(700, txt_surf.get_width() + 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:

                        chat_history.append("Ти: " + text)
                        ai_response = get_ai_response(text)
                        chat_history.append("AI: " + ai_response)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

if __name__ == '__main__':
    start2_back()
while True:
    back.fill((240, 240, 240))

    pygame.display.update()

def draw_button(text, x, y, w, h, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_rect = pygame.Rect(x, y, w, h)

if button_rect.collidepoint(pygame.mouse.get_pos()):
    hover_color = (
        (min(color[0]+ 30, 255)),
        (min(color[1] + 30, 255)),
        (min(color[2]+ 30, 255))
    )

    pygame.draw.rect(back, hover_color, button_rect)
else:
    pygame.draw.rect(back, color, button_rect)
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    back.blit(text_surface, text_rect)

if button_rect.collidepoint(mouse):
    if click[0]:
        play_click_sound()
    pygame.time.wait(150)

if action:
        action()



def main_menu():
    while True:
        back.fill(white)
        button_x = width - 220
        buttonSet_y = 450
        buttonI_y = 300
        buttonS_y = 150
        button_w = 180
        button_h = 60

        draw_button("Start", button_x, buttonS_y, button_w, button_h, (100, 200, 100), start_game)
        draw_button("Info", button_x, buttonI_y, button_w, button_h, (200, 100, 100), info_game)
        draw_button("Settings", button_x, buttonSet_y, button_w, button_h, (200, 150, 100), settings_game)

        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        print("Info")
                        sys.exit()

        pygame.display.update()

def info_back():

    inf_image = pygame.image.load('img/inf.jpg')
    inf_image = pygame.transform.scale(inf_image, (800, 800))

    inc_image = pygame.image.load('img/cat_inf.png')
    inc_image = pygame.transform.scale(inc_image, (500, 500))

    #font_big = pygame.font.SysFont(None, 16)





    #pygame.display.update
    #pygame.time.delay(100)

    while True:
        back.fill((240, 240,240))
        back.blit(inf_image, (0,0))
        back.blit(inc_image, (480, 80))


        draw_button("Language", width // 2 - 90, height - 100 - 400, 180, 50, (63, 91, 120), toggle_language)

        #mouse_pos = pygame.mouse.get_pos()

        if current_language == 'en':
            display_text_from_file('res/informationEng.txt', text_size=24)
        else:

            display_text_from_file('res/information.txt', text_size=24)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if width // 2 - 90 <= mouse_pos[0] <= width // 2 - 90 + 180 and height - 100 <= mouse_pos[
                        1] <= height - 100 + 50:
                        toggle_language()

        pygame.display.update()



def toggle_music():
    global music_on
    if music_on:
        pygame.mixer.music.pause()
        music_on = False
    else:
        pygame.mixer.music.unpause()
        music_on = True

def settings_back():
    global music_on
    while True:
        back.fill((240, 240, 240))
        font_big = pygame.font.SysFont(None, 60)
        text = font_big.render('Set Screen', True, (50, 50, 50))
        text_rect = text.get_rect(center=(width // 2, height // 4))
        back.blit(text, text_rect)


        music_text = "Music: ON" if music_on else "Music: OFF"
        draw_button(music_text, width //2  - 150, height // 78, 300, 60,(100, 200, 100), toggle_music)

        draw_button('Menu', width // 2 - 150, height // 2, 300, 60, (100, 200, 100), return_to_main_menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


        pygame.display.update()


def load_music():
    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1, 0.0)
        #print("Music loaded and playing")
    except pygame.error as e:
       # print("Could not load music:", e)
        pass
    load_music()
    main_menu()

