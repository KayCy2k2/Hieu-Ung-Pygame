import pygame
import random

pygame.init()

# Các thông số về màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Effector - Tan rã")

# Số lượng viên gạch
brick_count = 100

# Lớp Brick
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))  # Màu đỏ
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = random.choice([-1, 1]) * random.randint(1, 3)
        self.speed_y = random.choice([-1, 1]) * random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > width:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed_y *= -1

bricks = pygame.sprite.Group()

# Tạo các viên gạch
for _ in range(brick_count):
    brick = Brick(random.randint(0, width), random.randint(0, height))
    bricks.add(brick)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            # Khi nhấn phím 'q', các viên gạch sẽ tan rã
            bricks.empty()

    screen.fill((255, 255, 255))  # Màu trắng

    bricks.update()
    bricks.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
