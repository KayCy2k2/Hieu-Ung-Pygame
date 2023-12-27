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
thickness = 10  # Độ dày dải băng
color = (255, 255, 255)  # Màu sắc dải băng (trắng)
rotation_speed = 0.01  # Tốc độ quay
rotation = 5  # Góc quay tổng cộng

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Xóa màn hình trước mỗi vòng lặp

    # Vẽ dải băng Mobius
    points = []
    for i in range(360):
        # Tính toán vị trí điểm trên dải băng Mobius
        x = math.cos(math.radians(i + angle)) * radius
        y = math.sin(math.radians(2 * (i + angle))) * radius

        # Di chuyển dải băng tới giữa màn hình
        x += width / 2
        y += height / 2

        points.append((int(x), int(y)))

    # Vẽ dải băng Mobius bằng cách nối các điểm lại với nhau
    pygame.draw.lines(screen, color, False, points, thickness)

    # Cập nhật góc quay và góc quay tổng cộng
    angle += rotation_speed
    rotation += rotation_speed

    # Kiểm tra nếu đã quay đủ 360 độ thì trừ đi 360 để bắt đầu lại từ đầu
    if rotation >= 360:
        rotation -= 360

    pygame.display.flip()

# Kết thúc chương trình khi thoát khỏi vòng lặp
pygame.quit()
