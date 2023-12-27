import pygame
import random

# Khởi tạo Pygame
pygame.init()

# Cấu hình màn hình
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chữ rơi và vỡ")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# Tạo chữ cái
letters = "0123456789+-*/"

# Lớp chữ rơi
class FallingLetter:
    def __init__(self):
        self.x = random.randint(0, width) # Vị trí ngẫu nhiên theo chiều ngang
        self.y = 0 # Vị trí bắt đầu từ trên cùng
        self.speed = random.randint(1, 5) # Tốc độ ngẫu nhiên
        self.letter = random.choice(letters) # Chữ cái ngẫu nhiên

    def update(self):
        self.y += self.speed # Di chuyển chữ xuống dưới

        if self.y > (height - 40): # Nếu chữ chạm đáy màn hình
            self.break_apart()

    def break_apart(self):
        for _ in range(10): # Tạo ra 10 kí tự con
            letter_piece = LetterPiece(self.x, self.y, random.choice(letters))
            letter_pieces.append(letter_piece)

        falling_letters.remove(self) # Xóa chữ cái rơi

    def draw(self):
        font_size = 50
        font = pygame.font.Font(None, font_size)
        text = font.render(self.letter, True, WHITE)
        screen.blit(text, (self.x, self.y))

# Lớp kí tự nảy lên
class LetterPiece:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.speed_x = random.randint(-5, 5) # Tốc độ ngẫu nhiên theo chiều ngang
        self.speed_y = random.randint(-10, -5) # Tốc độ ngẫu nhiên theo chiều dọc
        self.letter = letter

    def update(self):
        self.x += self.speed_x # Di chuyển kí tự theo chiều ngang
        self.y += self.speed_y # Di chuyển kí tự theo chiều dọc

    def draw(self):
        font_size = 30
        font = pygame.font.Font(None, font_size)
        text = font.render(self.letter, True, RED)
        screen.blit(text, (self.x, self.y))

falling_letters = [] # Danh sách chữ cái rơi
letter_pieces = [] # Danh sách kí tự con nảy lên

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tạo chữ cái rơi mới mỗi 0.5 giây
    if random.random() < 0.005:
        falling_letter = FallingLetter()
        falling_letters.append(falling_letter)

    # Cập nhật và vẽ chữ cái rơi
    for falling_letter in falling_letters:
        falling_letter.update()
        falling_letter.draw()

    # Cập nhật và vẽ kí tự con nảy lên
    for letter_piece in letter_pieces:
        letter_piece.update()
        letter_piece.draw()

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
