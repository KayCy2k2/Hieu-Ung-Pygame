import pygame
import random

# Khởi tạo pygame
pygame.init()

# Định nghĩa kích thước của cửa sổ
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Màu sắc
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Tạo một danh sách chứa các đối tượng sấm sét
lightnings = []

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Nếu người dùng nhấn chuột trái
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Lấy tọa độ x và y của con trỏ chuột
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Thêm một đối tượng sấm sét mới vào danh sách
            lightnings.append([(mouse_x, mouse_y)])

    # Xóa màn hình
    screen.fill(WHITE)

    # Vẽ các đối tượng sấm sét trên màn hình
    for lightning in lightnings:
        for i in range(len(lightning)):
            pygame.draw.circle(screen, YELLOW, lightning[i], 5)
            if i > 0:
                pygame.draw.line(screen, YELLOW, lightning[i-1], lightning[i], 2)

            # Di chuyển các điểm của sấm sét ngẫu nhiên
            lightning[i] = (lightning[i][0] + random.randint(-5, 5),
                            lightning[i][1] + random.randint(-5, 5))

            # Thêm một điểm mới vào sấm sét
            if i == len(lightning) - 1 and random.randint(0, 10) == 0:
                lightning.append((lightning[i][0] + random.randint(-30, 30),
                                  lightning[i][1] + random.randint(10, 30)))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc pygame
pygame.quit()
