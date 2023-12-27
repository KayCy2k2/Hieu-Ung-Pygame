import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước của cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng gió thổi")

# Màu sắc
white = (255, 255, 255)

# Tạo danh sách các phần tử di chuyển giống như gió thổi
leaves = []
for _ in range(100):
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    leaves.append([x, y])

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill(white)

    # Di chuyển các phần tử giống như gió thổi
    for leaf in leaves:
        leaf[1] += 1  # Tăng tọa độ y để di chuyển xuống
        pygame.draw.circle(screen, (0, 255, 0), leaf, 3)  # Vẽ phần tử giống như lá

        # Nếu phần tử đi qua khỏi màn hình, đặt lại tọa độ y
        if leaf[1] > height:
            leaf[1] = 0

    pygame.display.flip()

# Kết thúc game
pygame.quit()
