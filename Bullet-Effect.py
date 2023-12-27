import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600

# Tạo màn hình game
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("bullet effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Định nghĩa class cho sấm sét
class Lightning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([2, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5

# Tạo danh sách các sprite sấm sét
lightning_list = pygame.sprite.Group()

# Vòng lặp game
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Lấy vị trí chuột
            pos = pygame.mouse.get_pos()
            # Tạo một sprite sấm sét tại vị trí chuột
            lightning = Lightning(pos[0], pos[1])
            # Thêm sprite vào danh sách
            lightning_list.add(lightning)

    # Cập nhật và vẽ các sprite sấm sét
    lightning_list.update()
    screen.fill(BLACK)
    lightning_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
