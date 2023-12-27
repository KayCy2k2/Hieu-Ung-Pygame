import pygame
import time

pygame.init()

# Các cài đặt cho màn hình pygame
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Automatic Typing")

# Các thông số cho văn bản
text = "Wellcome to My Mini Game!!!"
font_size = 50
font = pygame.font.Font(None, font_size)
text_color = (255, 255, 255)

# Lấy kích thước của đoạn văn bản
text_surface = font.render(text, True, text_color)
text_width = text_surface.get_width()
text_height = text_surface.get_height()

# Tính toán vị trí để căn giữa
x = width // 2 - text_width // 2
y = height // 2 - text_height // 2

# Chia đoạn văn bản thành các từ riêng biệt
words = text.split(' ')

# Cài đặt tốc độ gõ
typing_speed = 0.2 # Giây

# Vòng lặp game
done = False
clock = pygame.time.Clock()

for i in range(len(words)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Kiểm tra nút Esc được nhấn
                done = True

    screen.fill((0, 0, 0))

    # In các từ một cách tuần tự
    word_surface = font.render(' '.join(words[:i+1]), True, text_color)
    screen.blit(word_surface, (x, y))
    pygame.display.flip()
    time.sleep(typing_speed)

    pygame.display.update()
    clock.tick(60)

# Hiển thị thông báo trước khi thoát
exit_message = "Press ESC to exit game..."
exit_font = pygame.font.Font(None, 30)
exit_text = exit_font.render(exit_message, True, (255, 255, 255))
screen.blit(exit_text, (width // 2 - exit_text.get_width() // 2, height // 2 + 50))
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Kiểm tra nút Esc được nhấn
                done = True

pygame.quit()
