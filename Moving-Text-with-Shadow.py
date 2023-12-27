import pygame
from pygame.locals import *
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Text with Shadow")

clock = pygame.time.Clock()

# Hàm vẽ hiệu ứng Text Shadow
def draw_text_shadow(text, font, x, y, color, shadow_color):
    # Vẽ bóng chữ
    shadow_surface = font.render(text, True, shadow_color)
    screen.blit(shadow_surface, (x + 2, y + 2))

    # Vẽ chữ gốc
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Vòng lặp chính
running = True
x = 100  # Vị trí ban đầu của chữ
shadow_x = x + 2 # Vị trí ban đầu của bóng chữ
speed = 2  # Tốc độ di chuyển của chữ

while running:
    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Cập nhật vị trí của chữ và bóng chữ
    x += speed
    shadow_x += speed

    # Nếu chữ đi ra khỏi màn hình, đặt lại vị trí ban đầu
    if x > screen_width:
        x = -200
        shadow_x = x + 2

    # Gọi hàm vẽ hiệu ứng Text Shadow
    font = pygame.font.Font(None, 36)
    draw_text_shadow("Hello World", font, x, 200, (255, 255, 255), (128, 128, 128))

    # Cập nhật màn hình
    pygame.display.flip()

    clock.tick(60)  # Giới hạn FPS

# Đóng Pygame
pygame.quit()
sys.exit()
