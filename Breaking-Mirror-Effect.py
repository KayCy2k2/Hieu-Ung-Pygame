import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breaking Mirror Effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lớp Brick
class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(20, 40)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Danh sách các viên gạch
bricks = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tạo ra các viên gạch mới
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for _ in range(1):
        bricks.append(Brick(mouse_x, mouse_y))

    # Cập nhật và vẽ các viên gạch
    for brick in bricks:
        brick.update()
        brick.draw()

    # Loại bỏ các viên gạch đã vỡ
    bricks = [brick for brick in bricks if brick.size > 0]

    pygame.display.flip()
    clock.tick(1200)

# Kết thúc chương trình
pygame.quit()
