import pygame
import sys
import math

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lọc xoáy Pygame")

# Cấu hình màu sắc
background_color = (0, 0, 0)
line_color = (255, 255, 255)

# Cấu hình đối tượng lọc xoáy
angle = 0
angle_increment = 0.05
line_length = 200
center_x = screen_width // 2
center_y = screen_height // 2

# Vòng lặp chính
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    # Tính toán vị trí các đầu mút của đoạn thẳng
    x1 = center_x + int(math.cos(angle) * line_length)
    y1 = center_y + int(math.sin(angle) * line_length)
    x2 = center_x - int(math.cos(angle) * line_length)
    y2 = center_y - int(math.sin(angle) * line_length)

    # Vẽ đoạn thẳng
    pygame.draw.line(screen, line_color, (x1, y1), (x2, y2), 2)

    pygame.display.flip()
    angle += angle_increment

    clock.tick(120)

pygame.quit()
sys.exit()
