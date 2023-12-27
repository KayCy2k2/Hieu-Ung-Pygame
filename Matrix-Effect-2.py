import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Các thông số cửa sổ
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Matrix Rain")

# Các tham số ký tự
font_size = 20
font = pygame.font.Font(None, font_size)
chars = [chr(i) for i in range(33, 127)]
char_speed = 2

# Tạo danh sách chứa các ký tự rơi
falling_chars = []

class FallingChar:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(-height, 0)
        self.char = random.choice(chars)
        self.speed = random.randint(1, char_speed)

    def update(self):
        self.y += self.speed

        if self.y > height:
            self.y = random.randint(-height, 0)

    def draw(self):
        text_surface = font.render(self.char, True, (0, 255, 0))
        window.blit(text_surface, (self.x, self.y))

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))

    # Tạo và cập nhật các ký tự rơi
    for char in falling_chars:
        char.update()
        char.draw()

    # Thêm ký tự mới vào danh sách
    if len(falling_chars) < width // font_size:
        falling_chars.append(FallingChar())

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
