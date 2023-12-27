import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Vỡ Gương")

# Màu sắc
white = (255, 255, 255)

# Tạo hạt vỡ
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 10)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.lifetime = 30

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += 0.1  # Gravitational effect
        self.lifetime -= 1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

# Hàm chính
def main():
    running = True
    particles = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        particles.append(Particle(mouse_x, mouse_y))

        screen.fill(white)

        for particle in particles:
            particle.update()
            particle.draw()
            if particle.lifetime <= 0:
                particles.remove(particle)

        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()

if __name__ == "__main__":
    main()
