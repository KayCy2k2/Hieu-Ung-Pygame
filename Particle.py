import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Màu sắc
BLACK = (0, 0, 0)

# Số lượng hạt bụi
num_particles = 1000

# Lớp hạt bụi
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=pos)
        self.vel = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(1, 5)

    def update(self):
        self.rect.move_ip(self.vel)
        if not screen.get_rect().contains(self.rect):
            self.kill()

# Danh sách chứa các hạt bụi
particles = pygame.sprite.Group()

# Tạo ra các hạt bụi ban đầu
for _ in range(num_particles):
    particle = Particle((width / 2, height / 2))
    particles.add(particle)

clock = pygame.time.Clock()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa nền với màu trắng
    screen.fill((255, 255, 255))

    # Cập nhật và vẽ các hạt bụi
    particles.update()
    particles.draw(screen)

    # Cập nhật cửa sổ hiển thị
    pygame.display.flip()
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
