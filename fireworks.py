import pygame
import random

# Khởi tạo Pygame
pygame.init()
pygame.mixer.init()  # Khởi tạo bộ trộn âm thanh

# Tải âm thanh
a1 = pygame.mixer.Sound(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\single-firework-79814.mp3") # link: https://pixabay.com/vi/sound-effects/single-firework-79814/
a2 = pygame.mixer.Sound(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\tiny_rocketwav-14647.mp3") # link: https://pixabay.com/vi/sound-effects/tiny-rocketwav-14647/
# Lưu ý: nhớ chỉnh lại phần âm thanh, lên trang pixabay.com tải âm thanh về

# Cấu hình màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng pháo hoa")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Lớp pháo hoa
class Firework:
    def __init__(self):
        self.x = random.randint(100, width - 100) # Vị trí ngẫu nhiên theo chiều ngang
        self.y = height # Bắt đầu từ dưới cùng
        self.exploded = False # Trạng thái pháo hoa đã nổ hay chưa
        self.particles = [] # Danh sách các hạt pháo hoa
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) # Màu sắc ngẫu nhiên
    
    def explode(self):
        for _ in range(30): # Tạo ra 100 hạt pháo hoa
            particle = Particle(self.x, self.y, self.color)
            self.particles.append(particle)
        
        self.exploded = True
        
    def update(self):
        if not self.exploded: # Di chuyển pháo hoa lên trên màn hình
            self.y -= 10
            
            if self.y <= random.randint(200, 400): # Khi pháo hoa về một độ cao nhất định, nổ
                a1.play()  # Phát âm thanh lên khi pháo hoa nổ
                a1.set_volume(100)
                self.explode()
        else:
            for particle in self.particles:
                particle.update()

    def draw(self):
        if not self.exploded: # Vẽ pháo hoa chưa nổ
            pygame.draw.circle(screen, self.color, (self.x, int(self.y)), 10)
        else:
            for particle in self.particles:
                particle.draw()

# Lớp hạt pháo hoa
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = random.uniform(-5, 5) # Tốc độ ngẫu nhiên theo chiều ngang
        self.speed_y = random.uniform(-1, -10) # Tốc độ ngẫu nhiên theo chiều dọc
        self.size = random.uniform(1, 6) # Kích thước ngẫu nhiên
    
    def update(self):
        self.x += self.speed_x # Di chuyển hạt pháo hoa theo chiều ngang
        self.y += self.speed_y # Di chuyển hạt pháo hoa theo chiều dọc
        
        self.speed_y += 0.05 # Tạo độ rơi
        
        if self.size > 0.1: # Giảm kích thước hạt pháo hoa
            self.size -= 0.1
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

fireworks = [] # Danh sách pháo hoa

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("Times New Roman", size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        draw_text(screen, "HAPPY NEW YEARS 2024", 50, width // 2, height // 2 - 30)
        draw_text(screen, "Group Lập Trình Python", 40, width // 2, height // 2 + 40)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        if random.random() < 0.1: # Điều kiện để tạo ra một pháo hoa mới
            firework = Firework()
            a2.play()  # Phát âm thanh lên khi pháo hoa bay lên
            a2.set_volume(0.1)
            fireworks.append(firework)
                
        for firework in fireworks:
            firework.update()
            firework.draw()

        pygame.display.update()
        clock.tick(120)

    pygame.quit()

if __name__ == "__main__":
    main()    
