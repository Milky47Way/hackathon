import pygame
import openai
import sys
import os
from lab import lab_map, draw_lab, player_position, goal_position
#from quest import
#from hero import

#для ші
openai.api_key = ('gpt:AU54YW8RRi4TXANWp060hfjiJxU6btLIvPmqxAgYF0QLgPDwmNfdLT5NyC9Y8r_u4QZeQmwhzFJFkblB3T4yhgCdA9W2KZIQwDchnwN-SRJKHph3pqraKQNsAmcDeSXdm_4aNY-8_3oiLFalGXckzNJlfA-T')

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Ти мила аніме-дівчина в отоме грі."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Ти мила аніме-дівчина в отоме грі."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

#сцена, музика
width = 800
height = 600
total_score = 0

back = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Draconic Age')
icon = pygame.image.load('../Dragon.png')
pygame.display.set_icon(icon)

pygame.init()
pygame.mixer.init()

music_on = True
music_path = os.path.join(os.path.dirname(__file__), "res/Angels Airwaves - The Adventure.mp3")

white = (255, 255, 255)
black = (0,0,0)
gray = (200, 200, 200)
total_score = 0

def some_game_event():
    global total_score
    total_score += 10

def add_score(points):
    global total_score
    total_score += points

def draw_score(surface):
    font = pygame.font.SysFont(None, 40)  # Выбираем шрифт
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Создаём текст с текущими баллами
    surface.blit(score_text, (10, 10))

def scoreS():
    try:
        with open ('../res/score.txt', 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_score(score):
    with open('../res/score.txt', 'w') as f:
        f.write(str(score))

font = pygame.font.SysFont(None, 60)

box = pygame.Rect(50, 500, 700, 50)
color_inactive = gray
color_active = (0, 255, 0)
color = color_inactive
active = False
text = ''
chat_history = []

current_language = 'ua'

def draw_chat():
    y = 50
    for msg in chat_history[-10:]:
        msg_surface = font.render(msg, True, black)
        back.blit(msg_surface, (50, y))
        y += 30

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
        draw_button("Labyrinth", width // 2 - 150, height // 2 + 20, 300, 60, (100, 200, 100), start1_back)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()

def open_que():
    show_queue_window()

def show_queue_window():
    queue_window = pygame.Surface((300, 300))
    queue_window.fill((66, 255, 255))

    font4 = pygame.font.SysFont('Verdana', 40)
    try:
        with open('../res/lab.txt', 'r', encoding ='utf-8') as f:

            labInf = f.readlines()
    except FileNotFoundError:
        pass

    oy = 20
    for line in labInf:
        text = font4.render(line.strip(), True, (50, 50, 50))
    queue_window.blit(text, (10, oy))
    oy += 30

    back.blit(queue_window, (0, 150))
    pygame.display.update()

    window_open = True
    while window_open:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    window_open = False
        pygame.display.update()


def player_reaches_goal(player_position, goal_position):
    # Проверяем, достиг ли игрок цели (например, через координаты)
    if player_position == goal_position:
        return True

    return False

# Пример карты лабиринта



#меню лабіринт
def start1_back():
    global score

    lab_image = pygame.image.load('../img/inf.jpg')
    lab_image = pygame.transform.scale(lab_image, (800, 800))
    score = 0
    total_score = 0
    session_score = 0

    while True:
        back.blit(lab_image, (0, 0))

        draw_lab(back, lab_map)
        draw_score(back)
        add_score(10)
        if player_reaches_goal(player_position, goal_position):
            add_score(50)

        session_score += 1
        total_score += session_score
        save_score(total_score)
        print('За сессію:', session_score)
        print('всього:', total_score)
        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render('Start', True, (50, 50, 50))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        back.blit(text, text_rect)
        draw_button('Menu', width // 2 - 350, height // 2 - 200, 150, 60, (100, 200, 100), return_to_main_menu)
        draw_circle_button('?', width // 2 - 350, height // 2 + 200, 30, (100, 200, 100), open_que)
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
    while True:
        back.fill((240, 240, 240))

        font_big = pygame.font.SysFont(None, 80)
        text = font_big.render('', True, (50, 50, 50))
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

        pygame.display.update()
def draw_circle_button(text, x, y, radius, color, action=None, alpha=0):
    circle_surface = pygame.Surface((radius *  2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(circle_surface, (*color,alpha), (radius, radius), radius)
    back.blit(circle_surface, (x - radius, y - radius))

    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(text, True, (158, 189, 230))
    text_rect = text_surface.get_rect(center=(x, y))
    back.blit(text_surface, text_rect)

    for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
        if event.button == 1:
            mouse_x, mouse_y = event.pos
            if (mouse_x - x) ** 2 + (mouse_y - y) ** 2 <= radius**2:
                if action:
                    action()


def draw_button(text, x, y, w, h, color, action=None):
    pygame.draw.rect(back, color, (x, y, w, h))
    font = pygame.font.SysFont(None, 36)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    back.blit(text_surface, text_rect)

    if action:
        if pygame.mouse.get_pressed()[0]:
            if pygame.Rect(x, y, w, h).collidepoint(pygame.mouse.get_pos()):
                action()

def return_to_main_menu():
    pass

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

    inf_image = pygame.image.load('../img/inf.jpg')
    inf_image = pygame.transform.scale(inf_image, (800, 800))

    inc_image = pygame.image.load('../img/cat_inf.png')
    inc_image = pygame.transform.scale(inc_image, (500, 500))

    while True:
        back.fill((240, 240,240))
        back.blit(inf_image, (0,0))
        back.blit(inc_image, (480, 80))


        draw_button("Language", width // 2 - 90, height - 100 - 400, 180, 50, (63, 91, 120), toggle_language)
        draw_circle_button("Okay", width // 2, height - 100 - 320, 46, (63, 91, 120), return_to_main_menu, alpha=0 )


        if current_language == 'en':
            display_text_from_file('../res/informationEng.txt', text_size=24)
        else:

            display_text_from_file('../res/information.txt', text_size=24)

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

    global total_score
    global music_on
    font_big = pygame.font.SysFont(None, 60)


    score_text = font_big.render(f'score {total_score}', True, (255, 50, 50))
    score_rect = score_text.get_rect(center=(width // 2, height //2 + 150))

    while True:
        back.fill((240, 240, 240))
        back.blit(score_text, score_rect)

        music_text = "Music: ON" if music_on else "Music: OFF"
        draw_button(music_text, width //560 - 10, height // 78, 300, 60,(100, 200, 100), toggle_music)

        draw_button('Menu', width // 2 - 150, height // 2, 300, 60, (100, 200, 100), return_to_main_menu)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return


        pygame.display.update()
def return_to_main_menu():
    main_menu()

def load_music():

    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1, 0.0)
        print("Music loaded and playing")
    except pygame.error as e:
        print("Could not load music:", e)

load_music()
main_menu()

