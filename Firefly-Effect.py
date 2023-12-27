import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ và màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Firefly-Effect")
clock = pygame.time.Clock()

# Khởi tạo danh sách các hạt bụi
dust_particles = []
for _ in range(2000):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(1, 5)
    dust_particles.append([x, y, size])

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Xóa màn hình

    # Cập nhật và vẽ các hạt bụi
    for particle in dust_particles:
        x, y, size = particle
        if size > 0:
            pygame.draw.circle(screen, (255, 255, 255), (x, y), size)
            particle[0] += random.randint(-1, 1)
            particle[1] += random.randint(-1, 1)
            particle[2] -= 0.1

    pygame.display.flip()
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
