import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cấu hình kích thước màn hình
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ray-Effect-2")

# Thiết lập các màu
BLACK = (0, 0, 0)

# Tạo danh sách để lưu trữ tọa độ của sấm sét
lightning_coords = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Khi nhấp chuột, tạo một flash sáng ngẫu nhiên tại vị trí chuột
            x, y = pygame.mouse.get_pos()
            lightning_coords.append((x, y))

    # Xóa màn hình
    screen.fill(BLACK)

    # Vẽ các flash sáng sấm sét đã được lưu trữ
    for coord in lightning_coords:
        x, y = coord
        # Vẽ đường thẳng màu trắng từ vị trí chuột tới một điểm ngẫu nhiên
        pygame.draw.line(screen, (255, 255, 255), (x, y), (random.randint(0, width), random.randint(0, height)))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc pygame
pygame.quit()
