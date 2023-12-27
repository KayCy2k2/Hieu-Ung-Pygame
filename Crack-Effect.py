import pygame
import sys
import math
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Crack Effect")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tốc độ nứt
crack_speed = 3

# Điểm chạm ban đầu
crack_x, crack_y = width // 2, height // 2

# Danh sách lưu trữ các điểm nứt
crack_points = [(crack_x, crack_y)]

# Hàm tính toán điểm tiếp theo trên vết nứt
def calculate_next_point(last_point):
    angle = random.uniform(0, math.pi * 2)
    distance = random.randint(1, 10)
    next_x = last_point[0] + distance * math.cos(angle)
    next_y = last_point[1] + distance * math.sin(angle)
    return int(next_x), int(next_y)

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tính toán điểm tiếp theo trên vết nứt
    next_point = calculate_next_point(crack_points[-1])
    crack_points.append(next_point)

    # Xóa màn hình
    screen.fill(BLACK)

    # Vẽ các điểm nứt
    for point in crack_points:
        pygame.draw.circle(screen, WHITE, point, 1)

    # Cập nhật màn hình
    pygame.display.flip()

    # Giới hạn số lần lặp để tránh vết nứt quá dài
    if len(crack_points) > 500:
        running = False

    # Tạo tốc độ của vết nứt
    pygame.time.delay(crack_speed)

# Đóng cửa sổ khi kết thúc
pygame.quit()
sys.exit()
