import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shattered Mirror")

# Hình ảnh gương
mirror_image = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")
mirror_rect = mirror_image.get_rect(center=(width/2, height/2))

# Mảnh vỡ
shards = []
num_shards = 100

for _ in range(num_shards):
    shard = {
        "image": pygame.Surface((10, 10)),
        "rect": pygame.Rect(0, 0, 10, 10),
        "x_speed": pygame.Vector2(0, 0),
        "y_speed": pygame.Vector2(0, 0)
    }
    shard["image"].fill((255, 255, 255))
    shards.append(shard)

# Các vector tốc độ
x_speeds = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
y_speeds = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mirror_rect.collidepoint(mouse_pos):
                for shard in shards:
                    shard["rect"].center = mirror_rect.center
                    shard["x_speed"].x = random.choice(x_speeds)
                    shard["y_speed"].y = random.choice(y_speeds)

    # Cập nhật vị trí của các mảnh vỡ
    for shard in shards:
        shard["rect"].x += shard["x_speed"].x
        shard["rect"].y += shard["y_speed"].y

    # Vẽ hình ảnh gương
    screen.blit(mirror_image, mirror_rect)

    # Vẽ các mảnh vỡ
    for shard in shards:
        pygame.draw.rect(screen, (255, 255, 255), shard["rect"])

    pygame.display.flip()

# Kết thúc chương trình
pygame.quit()
