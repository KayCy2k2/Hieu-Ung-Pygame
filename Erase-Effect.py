import pygame
from pygame.locals import *

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("erase effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Tải hình ảnh gương
mirror_image = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")
mirror_rect = mirror_image.get_rect()
mirror_width, mirror_height = mirror_rect.width, mirror_rect.height

# Tạo danh sách các vết nứt
cracks = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Vẽ gương lên màn hình
    screen.blit(mirror_image, (10, 10))

    # Kiểm tra xem chuột có chạm vào gương không
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pos[0] >= 10 and mouse_pos[0] <= 10 + mirror_width and mouse_pos[1] >= 10 and mouse_pos[1] <= 10 + mirror_height:
        # Khi chuột chạm vào gương, thêm vết nứt vào danh sách
        cracks.append(mouse_pos)

    # Vẽ các vết nứt lên màn hình
    for crack in cracks:
        pygame.draw.circle(screen, WHITE, crack, 5)

    pygame.display.flip()
    clock.tick(60)

# Kết thúc chương trình
pygame.quit()
