
import pygame

pygame.init()

def render_image(window, img_path, point):
    img = pygame.image.load(img_path)
    window.blit(img, (point.x, point.y))

def render_text(window, text, point):

    font = pygame.font.SysFont("arial", 20)
    text = font.render(text, True, (0, 0, 0))

    text_rect = text.get_rect()
    text_rect.center = (point.x, point.y)

    window.blit(text, text_rect)

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Text_Box():

    def __init__(self, tl_point):
        # Positioning
        self.tl_point = tl_point
        self.input_rect = pygame.Rect(self.tl_point.x, self.tl_point.y, 140, 32)
        # Render colors
        self.color_active = pygame.Color('darkgray')
        self.color_passive = pygame.Color('lightgray')
        self.color = self.color_passive
        self.active = False
        # Render text
        self.user_text = ""
        self.base_font = pygame.font.Font(None, 32)

    def on_click(self, event):
        if event.type == pygame.KEYDOWN:
            if self.active and event.key == pygame.K_BACKSPACE:
                # Get text input from 0 to -1 i.e. end
                self.user_text = self.user_text[:-1]
            else:
                if self.active == True:
                    self.user_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
            elif not self.input_rect.collidepoint(event.pos):
                self.active = False
                self.color = self.color_passive

    def render(self, window):
        pygame.draw.rect(window, self.color, self.input_rect)
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        window.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        self.input_rect.w = max(100, text_surface.get_width() + 10)

    def get_current_text(self):
        return self.user_text

class Widget():

    def __init__(self, height, width, tl_point):
        self.height = height
        self.width = width
        self.tl_point = tl_point

    def render(self, window):
        # Create border rectangle
        pygame.draw.rect(window, (0, 0, 0), (self.tl_point.x, self.tl_point.y, self.width, self.height), border_radius=5)
        pygame.draw.rect(window, (255, 255, 255), (self.tl_point.x + 5, self.tl_point.y + 5, self.width - 10, self.height - 10), border_radius=5)

window = pygame.display.set_mode((500,500))

text_box = Text_Box(Point(50, 50))
clock = pygame.time.Clock()

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        
        text_box.on_click(event)

    window.fill((255, 255, 255))
    text_box.render(window)
    # render_image(window, "burgerstand.png", Point(0, 0))
    # widget = Widget(300, 200, Point(50, 50))

    # widget.render(window)
    # render_text(window, "Hello World", Point(100, 100))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()