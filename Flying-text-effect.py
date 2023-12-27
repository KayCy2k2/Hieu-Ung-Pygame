import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
width = 800
height = 600

# Màu sắc
black = (0, 0, 0)

# Tạo cửa sổ
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hiệu ứng chữ bay")

# Định nghĩa font chữ
font = pygame.font.Font(None, 24)

# Vị trí ban đầu của chữ
x = width // 2
y = height // 2

# Tạo danh sách các chữ cái
letters = [chr(i) for i in range(65, 91)]  # A-Z

# Hàm tạo vận tốc di chuyển ngẫu nhiên
def get_random_velocity():
    return random.randint(1, 1), random.randint(1, 1)

# Vận tốc ban đầu
vx, vy = get_random_velocity()

# Tạo biến text trước
text = font.render("Hello, World!", True, (255, 255, 255))

# Tốc độ di chuyển
speed = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_UP:
                speed += 0.5
            elif event.key == pygame.K_DOWN:
                speed -= 0.5

    # Cập nhật vị trí của chữ
    x += int(vx * speed)
    y += int(vy * speed)

    # Kiểm tra va chạm với biên của cửa sổ
    if x < 0 or x + text.get_width() > width:
        vx = -vx
    if y < 0 or y + text.get_height() > height:
        vy = -vy

    # Xóa màn hình
    window.fill(black)

    # Vẽ chữ lên màn hình
    window.blit(text, (x, y))

    # Hiển thị thông báo tốc độ
    speed_text = font.render(f"Speed: {speed}", True, (255, 255, 255))
    window.blit(speed_text, (10, 10))

    # Hiển thị thông báo thoát màn hình
    exit_text = font.render("Press ESC to exit", True, (255, 255, 255))
    window.blit(exit_text, (10, height - 40))

    # Cập nhật màn hình
    pygame.display.flip()

# Kết thúc Pygame
pygame.quit()
