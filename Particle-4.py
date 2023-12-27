import pygame
import random

# Khởi tạo pygame
pygame.init()

# Định nghĩa kích thước cửa sổ
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng khói")

# Tạo danh sách các hạt khói
particles = []

# Hàm tạo một hạt khói mới
def create_particle(x, y):
    particle = {
        'position': [x, y],
        'size': random.randint(10, 20),
        'color': (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)),
        'speed': [random.random() * 2 - 1, -random.random() * 2]
    }
    particles.append(particle)

# Vòng lặp chính
running = True
while running:
    screen.fill((0, 0, 0))  # Xóa màn hình
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Khi nhấn chuột
            x, y = pygame.mouse.get_pos()
            create_particle(x, y)

    # Cập nhật và vẽ các hạt khói
    for particle in particles:
        particle['position'][0] += particle['speed'][0]
        particle['position'][1] += particle['speed'][1]
        particle['size'] -= 0.1
        pygame.draw.circle(screen, particle['color'], [int(particle['position'][0]), int(particle['position'][1])], int(particle['size']))
        
        # Xóa các hạt khói đã mờ đi
        if particle['size'] <= 0:
            particles.remove(particle)

    pygame.display.flip()  # Cập nhật màn hình

# Kết thúc pygame
pygame.quit()
