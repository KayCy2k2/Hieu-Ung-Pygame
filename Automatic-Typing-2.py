import pygame
import time

class AutomaticTyping:
    def __init__(self):
        pygame.init()

        # Các cài đặt cho màn hình pygame
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Automatic Typing")

        # Các thông số cho văn bản
        self.text = "Wellcome to My Mini Game!!!"
        self.font_size = 40
        self.font = pygame.font.Font(None, self.font_size)
        self.text_color = (0, 255, 0)

        # Lấy kích thước của đoạn văn bản
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_width = self.text_surface.get_width()
        self.text_height = self.text_surface.get_height()

        # Tính toán vị trí để căn giữa
        self.x = self.width // 2 - self.text_width // 2
        self.y = self.height // 2 - self.text_height // 2

        # Chia đoạn văn bản thành các từ riêng biệt
        self.words = self.text.split(' ')

        # Cài đặt tốc độ gõ
        self.typing_speed = 0.3  # Giây

    def run(self):
        # Vòng lặp game
        done = False
        clock = pygame.time.Clock()

        for i in range(len(self.words)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Kiểm tra nút Esc được nhấn
                        done = True

            self.screen.fill((0, 0, 0))

            # In các từ một cách tuần tự
            word_surface = self.font.render(' '.join(self.words[:i + 1]), True, self.text_color)
            self.screen.blit(word_surface, (self.x, self.y))
            pygame.display.flip()
            time.sleep(self.typing_speed)

            pygame.display.update()
            clock.tick(60)

        # Hiển thị thông báo trước khi thoát
        exit_message = "Press ESC to exit game..."
        exit_font = pygame.font.Font(None, 20)
        exit_text = exit_font.render(exit_message, True, (255, 0, 0))
        self.screen.blit(exit_text, (self.width // 2 - exit_text.get_width() // 2, self.height // 2 + 250))
        pygame.display.flip()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Kiểm tra nút Esc được nhấn
                        done = True

        pygame.quit()

# Sử dụng class trong chương trình khác
typing_game = AutomaticTyping()
typing_game.run()
