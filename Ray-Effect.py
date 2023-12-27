import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
screen_width = 800
screen_height = 600

# Tạo cửa sổ pygame
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ray effect")

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)

# Cấu hình sấm sét
lightning_thickness = 3
lightning_color = (255, 255, 0)

# Hàm vẽ sấm sét
def draw_lightning(start_pos, end_pos):
    pygame.draw.line(screen, lightning_color, start_pos, end_pos, lightning_thickness)

# Vòng lặp chính
running = True
while running:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Xoá màn hình
    screen.fill(black)
    
    # Lấy vị trí chuột
    mouse_pos = pygame.mouse.get_pos()
    
    # Hiệu ứng sấm sét
    if pygame.mouse.get_pressed()[0]:
        for _ in range(10):
            start_pos = mouse_pos
            end_pos = (random.randint(0, screen_width), random.randint(0, screen_height))
            draw_lightning(start_pos, end_pos)
    
    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc pygame
pygame.quit()
