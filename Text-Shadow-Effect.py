import pygame
from pygame.locals import *
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Text Shadow Effect")

clock = pygame.time.Clock()

# Hàm vẽ hiệu ứng Text Shadow
def draw_text_shadow(text, font, x, y, color, shadow_color):
    # Vẽ bóng mờ
    shadow_surface = font.render(text, True, shadow_color)
    screen.blit(shadow_surface, (x + 2, y + 2))

    # Vẽ văn bản gốc
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Vòng lặp chính
running = True
while running:
    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Gọi hàm vẽ hiệu ứng Text Shadow
    font = pygame.font.Font(None, 72)
    draw_text_shadow("Hello World", font, 300, 200, (255, 255, 255), (128, 128, 128))

    # Cập nhật màn hình
    pygame.display.flip()

    clock.tick(60)  # Giới hạn FPS

# Đóng Pygame
pygame.quit()
sys.exit()
