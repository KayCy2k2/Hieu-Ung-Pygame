import pygame
import random

# Khởi tạo pygame
pygame.init()

# Thiết lập kích thước cửa sổ và màu nền
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
background_color = (255, 255, 255)

# Tạo danh sách chứa các hạt sẽ được vẽ
particles = []

# Hàm tạo hạt mới
def create_particle(x, y):
    particle = {'x': x, 'y': y, 'size': random.randint(10, 200), 'color': (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}
    particles.append(particle)

# Game loop
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra xem người dùng đã nhấp chuột hay chưa
            if event.button == 1:  # Chuột trái
                # Tạo hạt mới tại vị trí chuột nhấp
                create_particle(*event.pos)

    # Xóa màn hình
    screen.fill(background_color)

    # Cập nhật và vẽ các hạt
    for particle in particles:
        # Giảm kích thước của hạt
        particle['size'] -= 1
        if particle['size'] <= 0:
            particles.remove(particle)
        else:
            # Vẽ hạt
            pygame.draw.circle(screen, particle['color'], (particle['x'], particle['y']), particle['size'])

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc chương trình
pygame.quit()
