import pygame
import numpy as np

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mirror Shatter Effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Số lượng miếng ghép
num_pieces = 50

# Kích thước miếng ghép
piece_size = width // num_pieces

# Tạo ma trận piece_map
piece_map = np.ones((num_pieces, num_pieces))

# Lấy vị trí của miếng ghép nơi người dùng chạm vào màn hình
def get_piece_indices(pos):
    return pos[0] // piece_size, pos[1] // piece_size

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Lấy vị trí người dùng chạm vào màn hình
            mouse_pos = pygame.mouse.get_pos()

            # Lấy vị trí miếng ghép tương ứng với vị trí người dùng chạm vào
            piece_x, piece_y = get_piece_indices(mouse_pos)

            # Cập nhật ma trận piece_map bằng cách đặt giá trị của miếng ghép tương ứng thành 0 (vỡ)
            piece_map[piece_x, piece_y] = 0

    # Vẽ các miếng ghép
    for i in range(num_pieces):
        for j in range(num_pieces):
            if piece_map[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i * piece_size, j * piece_size, piece_size, piece_size))

    pygame.display.flip()
    clock.tick(60)

# Kết thúc chương trình
pygame.quit()
