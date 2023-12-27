import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng khói")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

def create_smoke_particles(position):
    particles = []
    for _ in range(20):
        particle = [position[0], position[1], random.randint(4, 8)]
        particle[2] *= 0.1
        particle.append(random.randint(1, 10) / 10)
        particles.append(particle)
    return particles

running = True
clock = pygame.time.Clock()

# Khởi tạo biến particles rỗng ban đầu
particles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Tạo hiệu ứng khói mới và gán lại giá trị cho particles
            particles = create_smoke_particles((x, y))

    screen.fill(BLACK)

    for particle in particles:
        particle[1] -= particle[2]
        pygame.draw.circle(screen, GRAY, (int(particle[0]), int(particle[1])), int(particle[2]))
        particle[2] += 0.05
        particle[3] -= 0.01

    particles = [p for p in particles if p[3] > 0]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
