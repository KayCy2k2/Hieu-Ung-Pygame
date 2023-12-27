import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)

# Tạo danh sách các tia sét
lightnings = []

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Kiểm tra xem người dùng có chạm vào màn hình không
    if pygame.mouse.get_pressed()[0] == 1:  # 1 tương ứng với giá trị True của chuột trái
        mouse_pos = pygame.mouse.get_pos()
        
        # Tạo một tia sét tại vị trí chuột
        lightning_color = (random.randint(150, 255), random.randint(150, 255), 255)  # Màu sét ngẫu nhiên
        lightning_radius = random.randint(10, 30)  # Bán kính của tia sét
        lightning_duration = random.randint(10, 30)  # Thời gian tồn tại của tia sét
        lightning = [mouse_pos, lightning_radius, lightning_duration, lightning_color]
        lightnings.append(lightning)
    
    # Xóa màn hình
    screen.fill(black)
    
    # Vẽ tất cả các tia sét
    for lightning in lightnings:
        pos, radius, duration, color = lightning
        
        # Vẽ tia sét
        pygame.draw.circle(screen, color, pos, radius)
        
        # Giảm thời gian tồn tại của tia sét
        lightning[2] -= 1
        
        # Xóa tia sét nếu đã tồn tại quá lâu
        if lightning[2] <= 0:
            lightnings.remove(lightning)
    
    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()
