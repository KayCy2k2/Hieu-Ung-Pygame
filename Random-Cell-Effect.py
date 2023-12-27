import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cài đặt kích thước cửa sổ
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("random cell effect")

# Số lượng khối nhỏ và các thông số tạo hình
BLOCK_SIZE = 40
ROWS = HEIGHT // BLOCK_SIZE
COLS = WIDTH // BLOCK_SIZE
blocks = []
for row in range(ROWS):
    for col in range(COLS):
        blocks.append(pygame.Rect(col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Màu sắc
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Hàm vẽ các khối nhỏ
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(win, GRAY, block)

# Hàm tạo hiệu ứng tan rã
def disintegrate_effect():
    for i in range(5):
        random.shuffle(blocks)
        for j, block in enumerate(blocks):
            if j % 2 == 0:
                pygame.draw.rect(win, WHITE, block)
            else:
                pygame.draw.rect(win, GRAY, block)
            pygame.display.update()
            pygame.time.wait(50)

# Vòng lặp chính
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        win.fill(WHITE)
        draw_blocks()
        disintegrate_effect()

    pygame.quit()

# Chạy chương trình
if __name__ == "__main__":
    main()
