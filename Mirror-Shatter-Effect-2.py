import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mirror Shatter Effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Lớp Shard
class Shard:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = WHITE
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.rotation = random.randint(0, 360)
        self.rotation_speed = random.randint(-3, 3)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rotation += self.rotation_speed

    def draw(self):
        rotated_image = pygame.transform.rotate(shard_image, self.rotation)
        new_size = int(self.size * 1.5)
        shard = pygame.transform.scale(rotated_image, (new_size, new_size))
        screen.blit(shard, (self.x - new_size/2, self.y - new_size/2))

# Hình ảnh fragment
shard_image = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")
shard_image = pygame.transform.scale(shard_image, (50, 50))

shards = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for _ in range(10):
            size = random.randint(20, 50)
            shard = Shard(mouse_pos[0], mouse_pos[1], size)
            shards.append(shard)

    # Cập nhật và vẽ các mảnh vỡ
    for shard in shards:
        shard.update()
        shard.draw()

    # Loại bỏ các mảnh vỡ ra khỏi danh sách
    shards = [shard for shard in shards if shard.size > 0]

    pygame.display.flip()
    clock.tick(60)

# Kết thúc chương trình
pygame.quit()
