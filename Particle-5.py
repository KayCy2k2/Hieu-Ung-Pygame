import pygame
import sys

# Khởi tạo pygame
pygame.init()

# Cấu hình cửa sổ game
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng sóng vỗ")
clock = pygame.time.Clock()

# Định nghĩa màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Lưu trữ danh sách các đối tượng sóng
waves = []

# Hàm để vẽ các đối tượng sóng lên màn hình
def draw_waves():
    for wave in waves:
        pygame.draw.circle(screen, wave[0], wave[1], wave[2])
        wave[2] += 1  # Tăng bán kính của đối tượng sóng theo thời gian
        if wave[2] >= 100:  # Nếu bán kính quá lớn, xóa đối tượng khỏi danh sách
            waves.remove(wave)

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Khi chạm vào màn hình
            pos = pygame.mouse.get_pos()
            waves.append([WHITE, pos, 0])  # Thêm một đối tượng sóng mới vào danh sách

    screen.fill(BLACK)  # Xóa nền màn hình
    draw_waves()  # Vẽ các đối tượng sóng lên màn hình
    pygame.display.flip()  # Cập nhật màn hình
    clock.tick(60)  # Giới hạn vòng lặp lại 60 lần/giây

# Kết thúc game
pygame.quit()
sys.exit()
