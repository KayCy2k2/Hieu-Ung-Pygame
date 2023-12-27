import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Glass Shatter Effect")

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Hình ảnh gương
glass_img = pygame.image.load(r"C:\Users\KayCy\OneDrive\Desktop\VSCode\Python\TD\a.png")  # Chỉnh đường dẫn tới file glass.png của bạn

# Class Fragment
class Fragment:
    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rotation = random.randint(0, 360)
        self.rotation_speed = random.uniform(-5, 5)
        self.scale = random.uniform(0.5, 1.5)
        self.alpha = 255

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rotation += self.rotation_speed

    def draw(self):
        fragment_img = pygame.transform.rotozoom(glass_img, self.rotation, self.scale)
        fragment_img.set_alpha(self.alpha)
        screen.blit(fragment_img, (self.x, self.y))

# Danh sách các Fragment
fragments = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for _ in range(5):
                speed_x = random.uniform(-5, 5)
                speed_y = random.uniform(-5, 5)
                fragments.append(Fragment(mouse_x, mouse_y, speed_x, speed_y))

    # Cập nhật và vẽ các Fragment
    for fragment in fragments:
        fragment.update()
        fragment.draw()
        fragment.alpha -= 5
        if fragment.alpha <= 0:
            fragments.remove(fragment)

    pygame.display.flip()
    clock.tick(120)

# Kết thúc chương trình
pygame.quit()
