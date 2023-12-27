import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng pháo hoa")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lớp pháo hoa
class Firework:
    def __init__(self):
        self.x = random.randint(100, width - 100) # Vị trí ngẫu nhiên theo chiều ngang
        self.y = height # Bắt đầu từ dưới cùng
        self.exploded = False # Trạng thái pháo hoa đã nổ hay chưa
        self.particles = [] # Danh sách các hạt pháo hoa
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) # Màu sắc ngẫu nhiên
    
    def explode(self):
        for _ in range(100): # Tạo ra 100 hạt pháo hoa
            particle = Particle(self.x, self.y, self.color)
            self.particles.append(particle)
        
        self.exploded = True
        
    def update(self):
        if not self.exploded: # Di chuyển pháo hoa lên trên màn hình
            self.y -= 5
            
            if self.y <= 200: # Khi pháo hoa về một độ cao nhất định, nổ
                self.explode()
        else:
            for particle in self.particles:
                particle.update()

    def draw(self):
        if not self.exploded: # Vẽ pháo hoa chưa nổ
            pygame.draw.circle(screen, self.color, (self.x, int(self.y)), 5)
        else:
            for particle in self.particles:
                particle.draw()

# Lớp hạt pháo hoa
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.randint(-5, 5) # Tốc độ ngẫu nhiên theo chiều ngang
        self.speed_y = random.randint(-15, -5) # Tốc độ ngẫu nhiên theo chiều dọc
        self.size = random.randint(2, 5) # Kích thước ngẫu nhiên
    
    def update(self):
        self.x += self.speed_x # Di chuyển hạt pháo hoa theo chiều ngang
        self.y += self.speed_y # Di chuyển hạt pháo hoa theo chiều dọc
        
        self.speed_y += 0.1 # Tạo tác động của trọng lực
        
        if self.size > 0.1: # Giảm kích thước hạt pháo hoa
            self.size -= 0.1
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

fireworks = [] # Danh sách pháo hoa

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN: # Tạo pháo hoa khi nhấp chuột
            firework = Firework()
            fireworks.append(firework)
            
    for firework in fireworks:
        firework.update()
        firework.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
