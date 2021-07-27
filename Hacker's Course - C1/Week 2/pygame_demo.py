
import pygame

pygame.init()

window_len = 500
window_wid = 500
window = pygame.display.set_mode((window_len, window_wid))

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

def render_text(window, text, point):

    font = pygame.font.SysFont("arial", 20)
    text = font.render(text, True, (0, 0, 0))

    text_rect = text.get_rect()
    text_rect.center = (point.x, point.y)

    window.blit(text, text_rect)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    window.fill((255, 255, 255))

    # Draw rect
    border_wid = 5
    pygame.draw.rect(window, (0, 0, 255), (100, 100, 100, 250))
    pygame.draw.rect(window, (0, 0, 255), (100  + border_wid, 100 + border_wid, 100 - border_wid * 2, 250 - border_wid * 2))

    pygame.draw.rect(window, (0, 0, 255), (100, 100, 100, 250))
    # Draw circle
    pygame.draw.circle(window, (0, 255, 0), (250, 250), 100)

    img = pygame.image.load("/Users/Desktop/KeenKiz-Hacker/Hacker's Course - C1/Week 2/burgerstand.png")
    window.blit(img, (0, 0))

    render_text(window, "Hello There", Point(250, 200))

    pygame.display.flip()
    
pygame.quit()