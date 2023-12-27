import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing-Ball-Effect-3")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Đối tượng hạt
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.color = WHITE
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)
        self.gravity = 0.1
        self.lifespan = 100

    def update(self):
        self.speed_y += self.gravity
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifespan -= 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Danh sách các hạt
particles = []

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill(BLACK)

    # Tạo ra hạt mới và thêm vào danh sách hạt
    particles.append(Particle(width // 2, height // 2))

    # Cập nhật và vẽ các hạt
    for particle in particles:
        particle.update()
        particle.draw()

    # Loại bỏ các hạt đã biến mất
    particles = [particle for particle in particles if particle.lifespan > 0]

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc pygame
pygame.quit()
