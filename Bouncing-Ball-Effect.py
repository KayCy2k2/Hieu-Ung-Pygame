import pygame
import random

pygame.init()

# Định nghĩa kích thước cửa sổ
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball effect")

clock = pygame.time.Clock()
FPS = 60

# Tạo danh sách các hạt pháo
particles = []

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(5, 20)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-15, -5)
        self.gravity = 0.5

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += self.gravity

    def draw(self):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.size)

    def is_alive(self):
        return self.size > 0

# Vòng lặp chính
running = True
while running:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            particles.append(Particle(*event.pos))

    for particle in particles:
        particle.update()
        particle.draw()

        # Kiểm tra xem hạt pháo có còn sống hay không
        if not particle.is_alive():
            particles.remove(particle)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
