import pygame
import random

# Khởi tạo chương trình Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Effect Demo")

# Tạo danh sách các hạt dưa hấu
particles = []
num_particles = 200

for _ in range(num_particles):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(5, 20)
    speed = [random.randint(-5, 5) / 10, random.randint(-5, 5) / 10]
    particles.append([x, y, size, speed])

# Vòng lặp chính
running = True
while running:
    screen.fill((0, 0, 0))

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Cập nhật vị trí và kích thước của các hạt dưa hấu
    for particle in particles:
        particle[0] += particle[3][0]
        particle[1] += particle[3][1]
        particle[2] -= 0.1

        if particle[2] <= 0:
            particle[0] = random.randint(0, width)
            particle[1] = random.randint(0, height)
            particle[2] = random.randint(5, 20)

    # Vẽ các hạt dưa hấu lên màn hình
    for particle in particles:
        pygame.draw.circle(screen, (255, 0, 100), (int(particle[0]), int(particle[1])), int(particle[2]))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc chương trình Pygame
pygame.quit()




