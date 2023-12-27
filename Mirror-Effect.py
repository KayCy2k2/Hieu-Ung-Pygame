import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mirror Effect")

# Màu sắc
BLACK = (0, 0, 0)

# Hình ảnh texture gương
mirror_img = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png").convert_alpha()
mirror_rect = mirror_img.get_rect(center=(width // 2, height // 2))

running = True
clock = pygame.time.Clock()

# Danh sách các vùng vỡ gương
fragments = []

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Kiểm tra nếu chuột chạm vào màn hình
            if mirror_rect.collidepoint(event.pos):
                # Tạo ra vùng vỡ gương
                for y in range(0, mirror_rect.height, 10):
                    for x in range(0, mirror_rect.width, 10):
                        xpos = mirror_rect.left + x
                        ypos = mirror_rect.top + y
                        fragment_rect = pygame.Rect(xpos, ypos, 10, 10)
                        fragment_speed = pygame.Vector2(random.uniform(-3, 3), random.uniform(-3, 3))
                        fragments.append((fragment_rect, fragment_speed))

    # Di chuyển và vẽ các vùng vỡ gương
    for fragment in fragments:
        fragment_rect, fragment_speed = fragment
        fragment_rect.move_ip(fragment_speed)
        pygame.draw.rect(screen, (255, 255, 255), fragment_rect)

    # Vẽ gương lên màn hình
    screen.blit(mirror_img, mirror_rect)

    pygame.display.flip()
    clock.tick(60)

# Kết thúc chương trình
pygame.quit()
