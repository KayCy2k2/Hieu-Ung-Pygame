import pygame
import math

# Khởi tạo màn hình pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mobius Strip Simulator")

# Các thông số cho hiệu ứng Mobius Strip
angle = 0  # Góc quay
radius = min(width, height) * 0.3  # Bán kính
speed = 0.01  # Tốc độ quay

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Xóa màn hình trước mỗi vòng lặp

    # Tính toán vị trí điểm trên dải băng Mobius
    x = math.cos(angle) * radius
    y = math.sin(2 * angle) * radius

    # Di chuyển dải băng tới giữa màn hình
    x += width / 2
    y += height / 2

    # Vẽ dải băng Mobius
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 5)

    # Cập nhật góc quay
    angle += speed

    pygame.display.flip()

# Kết thúc chương trình khi thoát khỏi vòng lặp
pygame.quit()
