import pygame
width = 800
height = 600
score = 0
back = pygame.display.set_mode((width, height))
lab_map = [
    [3, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 1],
]

CELL_SIZE = 38
OFFSET_X, OFFSET_Y = 160, 19


def draw_lab(surface, lab):
    wall_color =(255, 255, 255)
    rows = len(lab)
    cols = len(lab[0])

    for y in range(rows):
        for x in range(cols):
            if lab[y][x] == 1:
                cx = OFFSET_X + x * CELL_SIZE
                cy = OFFSET_Y + y * CELL_SIZE

                if y == 0 or lab[y-1][x] == 0:
                    pygame.draw.line(surface, wall_color, (cx, cy), (cx + CELL_SIZE, cy), 2)
                if y == rows - 1 or lab[y+1][x] == 0:
                    pygame.draw.line(surface, wall_color, (cx, cy + CELL_SIZE), (cx + CELL_SIZE, cy + CELL_SIZE), 2)
                if x == 0 or lab[y][x-1] == 0:
                    pygame.draw.line(surface, wall_color, (cx, cy), (cx, cy + CELL_SIZE), 2)
                if x == cols - 1 or lab[y][x+1] == 0:
                    pygame.draw.line(surface, wall_color, (cx + CELL_SIZE, cy), (cx + CELL_SIZE, cy + CELL_SIZE), 2)
score = 0
player_position = (0, 5)
goal_position = (10, 10)

