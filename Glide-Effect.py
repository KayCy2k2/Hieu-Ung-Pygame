import pygame
import random

# Kích thước màn hình
WIDTH = 800
HEIGHT = 600

# Màu sắc
WHITE = (255, 255, 255)

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gió thổi")

# Tạo danh sách chứa các đối tượng gió
wind_particles = []

class WindParticle:
    def __init__(self):
        self.x = WIDTH  # Vị trí x ban đầu của gió
        self.y = random.randint(0, HEIGHT)  # Vị trí y ngẫu nhiên của gió
        self.speed = random.randint(1, 3)  # Tốc độ di chuyển của gió

    def update(self):
        self.x -= self.speed  # Di chuyển gió sang trái

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), 2)  # Vẽ gió

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Tạo gió mới nếu số lượng gió hiện tại ít hơn 100
    if len(wind_particles) < 100:
        wind_particles.append(WindParticle())

    # Cập nhật và vẽ các đối tượng gió
    for particle in wind_particles:
        particle.update()
        particle.draw()
    
    pygame.display.flip()

# Đóng Pygame
pygame.quit()
