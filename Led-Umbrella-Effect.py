import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cấu hình màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("led umbrella effect")

# Hàm tạo một viên gạch
def create_brick(x, y):
    brick_size = 50
    brick_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(screen, brick_color, (x, y, brick_size, brick_size))

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))  # Xóa màn hình

    # Tạo các viên gạch với hiệu ứng tan rã
    for x in range(0, width, 50):
        for y in range(0, height, 50):
            create_brick(x, y)

            # Hiệu ứng tan rã - Loại bỏ một phần diện tích của viên gạch
            disintegrate_rate = 4  # Tỷ lệ làm mờ, càng lớn càng nhanh
            rect = pygame.Rect(x + disintegrate_rate, y + disintegrate_rate, 50 - disintegrate_rate*2, 50 - disintegrate_rate*2)
            pygame.draw.rect(screen, (0, 0, 0), rect)

    pygame.display.flip()  # Cập nhật màn hình

# Kết thúc pygame
pygame.quit()
