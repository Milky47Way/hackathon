import pygame
pygame.init()

CELL_SIZE = 38
OFFSET_X, OFFSET_Y = 160, 19  # зсув мапи на екрані
grid_x = (100 - OFFSET_X) // CELL_SIZE
grid_y = (500 - OFFSET_Y) // CELL_SIZE

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, size, width, height):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.back_width = width
        self.back_height = height

    def handle_input(self, lab_map):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = self.speed

        original_x, original_y = self.rect.x, self.rect.y
        self.rect.x += dx
        if self.collides_with_walls(lab_map):
            self.rect.x = original_x
        self.rect.y += dy
        if self.collides_with_walls(lab_map):
            self.rect.y = original_y


    def update(self, lab_map):
        self.handle_input(lab_map)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def collides_with_walls(self, lab_map):
        rows = len(lab_map)
        cols = len(lab_map[0])
        for y in range(rows):
            for x in range(cols):
                if lab_map[y][x] == 1:
                    wall_rect = pygame.Rect(
                        OFFSET_X + x * CELL_SIZE,
                        OFFSET_Y + y * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                    if self.rect.colliderect(wall_rect):
                        return True
        return False