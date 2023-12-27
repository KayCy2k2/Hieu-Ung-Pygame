import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước cửa sổ
width = 800
height = 600

# Tạo cửa sổ
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng Sấm sét")

# Màu sắc
WHITE = (255, 255, 0)
BLACK = (0, 0, 0)

# Hàm tạo sấm sét
def draw_lightning():
    for i in range(10):
        # Tọa độ ban đầu
        start_x = random.randint(400, 400)
        start_y = 0
        
        # Tạo mảng tọa độ các điểm trong sấm sét
        points = [(start_x, start_y)]
        
        # Tạo chiều dài sấm sét
        length = random.randint(10, 50)
        
        # Tạo sấm sét
        for _ in range(length):
            # Tạo tọa độ điểm tiếp theo
            next_x = points[-1][0] + random.randint(-10, 10)
            next_y = points[-1][1] + random.randint(5, 20)
            
            # Thêm vào mảng tọa độ điểm
            points.append((next_x, next_y))
        
        # Vẽ sấm sét lên màn hình
        pygame.draw.lines(screen, WHITE, False, points, 1)
        pygame.display.flip()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Xóa màn hình
    screen.fill(BLACK)
    
    # Tạo sấm sét khi nhấn chuột
    if pygame.mouse.get_pressed()[0] == 1:
        draw_lightning()
    
    # Cập nhật màn hình
    pygame.display.update()

# Kết thúc pygame
pygame.quit()
