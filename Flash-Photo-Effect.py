import pygame
import random

# Khởi tạo pygame
pygame.init()

# Cài đặt kích thước cửa sổ và các thông số cần thiết
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
smoke_images = [pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png"), pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")]  # Thay đổi 'smoke1.png' và 'smoke2.png' bằng các tệp hình ảnh của bạn

# Lớp Smoke để quản lý các hạt khói
class Smoke(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(smoke_images)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.fade = 255

    def update(self):
        self.fade -= 5
        if self.fade <= 0:
            self.kill()
        else:
            self.image.set_alpha(self.fade)

# Tạo danh sách chứa các hạt khói
smoke_group = pygame.sprite.Group()

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Xử lý sự kiện nhấp chuột
            x, y = pygame.mouse.get_pos()
            smoke = Smoke(x, y)
            smoke_group.add(smoke)

    screen.fill((0, 0, 0))  # Xóa màn hình

    # Cập nhật và vẽ các hạt khói
    smoke_group.update()
    smoke_group.draw(screen)

    pygame.display.flip()
    clock.tick(60)

# Kết thúc pygame
pygame.quit()
