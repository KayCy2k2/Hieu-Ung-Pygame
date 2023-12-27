import pygame
import random

# Khởi tạo pygame
pygame.init()

# Màn hình game
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shattered Mirror Effect")

# Màu sắc
WHITE = (255, 255, 255)

# Lớp Crystal
class Crystal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(10, 20)
        self.color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(-2, 2)
        self.rotation = random.randint(-5, 5)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Danh sách các viên pha lê
crystals = []

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for _ in range(30):
                crystals.append(Crystal(mouse_x, mouse_y))

    # Cập nhật và vẽ các viên pha lê
    for crystal in crystals:
        crystal.update()
        crystal.draw()

    # Loại bỏ các viên pha lê đã di chuyển ra khỏi màn hình
    crystals = [crystal for crystal in crystals if 0 <= crystal.x <= width and 0 <= crystal.y <= height]

    pygame.display.flip()
    clock.tick(60)

# Kết thúc chương trình
pygame.quit()
