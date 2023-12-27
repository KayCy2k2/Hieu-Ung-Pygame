import pygame
from math import sin, cos, radians

# Kích thước màn hình
WIDTH = 800
HEIGHT = 600

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Khởi tạo pygame
pygame.init()

# Tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mobius Strip")

# Vòng lặp chính
running = True
angle = 0

while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill(BLACK)

    # Tính toán tọa độ của điểm trên dải băng Mobius
    x = (cos(radians(angle)) * 100) + (sin(radians(2*angle)) * 100) + WIDTH/2
    y = (sin(radians(angle)) * 100) + (sin(radians(2*angle)) * 100) + HEIGHT/2

    # Vẽ điểm trên màn hình
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 2)

    # Cập nhật góc
    angle += 1

    # Cập nhật màn hình
    pygame.display.update()

# Kết thúc pygame
pygame.quit()
