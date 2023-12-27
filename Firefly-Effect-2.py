import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tan rã")

# Định nghĩa màu sắc
black = (0, 0, 0)
white = (255, 255, 255)

# Định nghĩa lớp Brick
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = 20

    def update(self):
        # Giảm kích thước của viên gạch
        self.size -= 1
        if self.size <= 0:
            self.kill()
        else:
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill(white)
            self.rect = self.image.get_rect(center=self.rect.center)

# Tạo danh sách các viên gạch
bricks = pygame.sprite.Group()

# Tạo ra các viên gạch ban đầu
for _ in range(50):
    x = random.randint(0, width)
    y = random.randint(0, height)
    brick = Brick(x, y)
    bricks.add(brick)

# Vòng lặp chính của game
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình
    screen.fill(black)

    # Cập nhật và vẽ các viên gạch
    bricks.update()
    bricks.draw(screen)

    # Cập nhật hiển thị
    pygame.display.flip()
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
