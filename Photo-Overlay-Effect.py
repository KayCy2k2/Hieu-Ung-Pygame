import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("photo overlay effect")

# Tải hình ảnh nứt từ file
crack_image = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Khi nhấp chuột, vẽ hình ảnh nứt tại vị trí chuột
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(crack_image, (mouse_x - crack_image.get_width() / 2, mouse_y - crack_image.get_height() / 2))

    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()
sys.exit()
