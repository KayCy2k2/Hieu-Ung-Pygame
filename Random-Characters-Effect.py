import pygame
from pygame.locals import *
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Characters Effect")

clock = pygame.time.Clock()

# Hàm vẽ kí tự
def draw_character(character, font, x, y, color):
    character_surface = font.render(character, True, color)
    screen.blit(character_surface, (x, y))

# Vòng lặp chính
running = True
characters = "Hello Wordl"  # Câu cần hiển thị
font_size = 36
font = pygame.font.Font(None, font_size)
character_positions = []  # Lưu trữ vị trí của từng kí tự
character_speeds = []  # Lưu trữ tốc độ di chuyển của từng kí tự
target_positions = []  # Lưu trữ vị trí cuối cùng của từng kí tự

# Khởi tạo các vị trí ban đầu và tốc độ di chuyển ngẫu nhiên cho từng kí tự
for i in range(len(characters)):
    x = random.randint(0, screen_width - font_size)
    y = random.randint(0, screen_height - font_size)
    character_positions.append((x, y))
    character_speeds.append((random.uniform(-5, 5), random.uniform(-5, 5)))
    target_positions.append((screen_width // 2 - len(characters) * font_size // 2 + i * font_size, screen_height // 2))

while running:
    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Cập nhật vị trí của từng kí tự
    for i in range(len(characters)):
        x, y = character_positions[i]
        dx, dy = character_speeds[i]
        target_x, target_y = target_positions[i]

        if (x < target_x):
            x += min(dx, target_x - x)
        elif (x > target_x):
            x += max(dx, target_x - x)

        if (y < target_y):
            y += min(dy, target_y - y)
        elif (y > target_y):
            y += max(dy, target_y - y)

        # Kiểm tra và giới hạn vị trí của kí tự trong màn hình
        x = max(0, min(screen_width - font_size, x))
        y = max(0, min(screen_height - font_size, y))

        # Kiểm tra và thay đổi hướng di chuyển khi kí tự chạm biên màn hình
        if x == 0 or x == screen_width - font_size:
            dx *= -2
        if y == 0 or y == screen_height - font_size:
            dy *= -2

        character_positions[i] = (x, y)
        character_speeds[i] = (dx, dy)

        # Gọi hàm vẽ kí tự
        draw_character(characters[i], font, x, y, (255, 0, 255))

    # Cập nhật màn hình
    pygame.display.flip()

    clock.tick(120)  # Giới hạn FPS

# Đóng Pygame
pygame.quit()
sys.exit()
