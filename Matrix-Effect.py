import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cài đặt kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Cài đặt màu sắc
black = (0, 0, 0)
green = (0, 255, 0)

# Cài đặt font chữ
font = pygame.font.Font(None, 36)

# Tạo danh sách các ký tự ma trận
matrix_chars = [chr(i) for i in range(33, 127)]

# Tạo danh sách các vụn ma trận
matrix_particles = []

# Hàm tạo vụn ma trận mới
def create_matrix_particle():
    x = random.randint(0, width)
    y = random.randint(0, height)
    char = random.choice(matrix_chars)
    speed = random.randint(1, 5)
    particle = {'x': x, 'y': y, 'char': char, 'speed': speed}
    matrix_particles.append(particle)

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill(black)

    # Tạo vụn ma trận mới
    if random.random() < 0.2:
        create_matrix_particle()

    # Cập nhật vị trí và vẽ các vụn ma trận
    for particle in matrix_particles:
        particle['y'] += particle['speed']
        text_surface = font.render(particle['char'], True, green)
        screen.blit(text_surface, (particle['x'], particle['y']))

    # Loại bỏ các vụn ma trận vượt quá khung
    matrix_particles = [particle for particle in matrix_particles if particle['y'] < height]

    # Cập nhật màn hình
    pygame.display.flip()

# Đóng cửa sổ Pygame
pygame.quit()
