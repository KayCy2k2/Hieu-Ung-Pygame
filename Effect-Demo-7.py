import pygame
from pygame.locals import *
import random

# Khởi tạo pygame
pygame.init()

# Cài đặt kích thước cửa sổ và tốc độ khung hình
screen_width = 800
screen_height = 600
fps = 60

# Tạo cửa sổ
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hiệu ứng vỡ kính')

# Tạo danh sách các mảnh vỡ
fragments = []
for i in range(100):
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(5, 20)
    speed_x = random.randint(-5, 5)
    speed_y = random.randint(-5, 5)
    fragments.append([x, y, size, speed_x, speed_y])

# Vòng lặp chính
running = True
clock = pygame.time.Clock()
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Di chuyển và vẽ mảnh vỡ
    for fragment in fragments:
        x, y, size, speed_x, speed_y = fragment
        x += speed_x
        y += speed_y
        pygame.draw.circle(screen, (255, 255, 255), (x, y), size)
        fragment[0] = x
        fragment[1] = y

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(fps)

# Kết thúc pygame
pygame.quit()
