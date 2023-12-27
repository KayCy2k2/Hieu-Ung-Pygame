import pygame
from pygame.locals import *
import sys
import random

# Khởi tạo Pygame
pygame.init()

# Thiết lập kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rainfall Effect")

clock = pygame.time.Clock()

# Hàm vẽ chữ cái
def draw_text(text, font, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Tạo danh sách các chữ cái
letters = "abcdefghijklmnopqrstuvwxyz"

# Thiết lập font chữ và kích thước
font_size = 36
font = pygame.font.Font(None, font_size)

# Tạo danh sách các chữ cái rơi
raindrops = []
for _ in range(100):
    x = random.randint(0, screen_width)
    y = random.randint(-screen_height, 0)
    speed = random.randint(2, 10)
    letter = random.choice(letters)
    raindrops.append([x, y, speed, letter, False])

running = True

while running:
    # Kiểm tra sự kiện
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Xóa màn hình
    screen.fill((0, 0, 0))

    # Cập nhật và vẽ chữ cái rơi
    for i in range(len(raindrops)):
        x, y, speed, letter, fallen = raindrops[i]
        
        if not fallen:
            y += speed

            # Kiểm tra và chỉnh lại vị trí chữ cái khi rơi xuống đáy màn hình
            if y > screen_height:
                y = screen_height
                speed = -speed
                fallen = True
        
        elif fallen and y < screen_height + font_size:
            y += speed

            # Kiểm tra và chỉnh lại vị trí chữ cái khi nảy lên
            if y <= 0 - font_size:
                y = random.randint(-screen_height, 0)
                x = random.randint(0, screen_width)
                speed = random.randint(2, 10)
                letter = random.choice(letters)
                fallen = False
        
        raindrops[i] = [x, y, speed, letter, fallen]

        # Vẽ chữ cái lên màn hình
        draw_text(letter, font, x, y, (255, 255, 255))

    pygame.display.update()
    clock.tick(60)

# Kết thúc Pygame
pygame.quit()
sys.exit()
