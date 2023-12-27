import pygame
import random

# Khởi tạo chương trình Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Effect Demo 2")

# Tải font chữ chứa ký tự trái tim
font_size = 20
heart_font = pygame.font.Font(None, font_size)
heart_char = "a"

# Tạo danh sách các hạt dưa hấu
particles = []
num_particles = 200

for _ in range(num_particles):
    x = random.randint(0, width)
    y = random.randint(0, height)
    speed = [random.randint(-5, 5) / 10, random.randint(-5, 5) / 10]
    particles.append([x, y, speed])

# Vòng lặp chính
running = True
while running:
    screen.fill((0, 0, 0))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật vị trí của các hạt dưa hấu
    for particle in particles:
        particle[0] += particle[2][0]
        particle[1] += particle[2][1]

        if particle[0] < -font_size or particle[0] > width or particle[1] < -font_size or particle[1] > height:
            particle[0] = random.randint(0, width)
            particle[1] = random.randint(0, height)

    # Vẽ các hạt dưa hấu lên màn hình
    for particle in particles:
        heart_surface = heart_font.render(heart_char, True, (255, 0, 100))
        screen.blit(heart_surface, (particle[0], particle[1]))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc chương trình Pygame
pygame.quit()
