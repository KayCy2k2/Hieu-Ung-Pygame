import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing-Ball-Effect-2")

# Màu sắc
BLACK = (0, 0, 0)

# Đối tượng hạt nhỏ
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.size = random.randint(5, 20)
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-15, -5)
        self.lifetime = 100
    
    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size)
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y += 1
        self.lifetime -= 1
        
# Hàm chạy trò chơi
def game_loop():
    running = True
    particles = []
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        win.fill(BLACK)
        
        # Tạo hạt mới
        if random.randint(0, 10) < 3:
            particles.append(Particle(WIDTH // 2, HEIGHT // 2))
            
        # Vẽ và cập nhật hạt
        for particle in particles:
            particle.draw()
            particle.update()
            if particle.lifetime <= 0:
                particles.remove(particle)
        
        pygame.display.update()

    pygame.quit()

# Chạy trò chơi
game_loop()

