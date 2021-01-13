#    comicFont = pygame.font.SysFont('Comic Sans MS', 30, True)
#    main_text = comicFont.render('Socket Chat',True , (0, 0, 0))
#    chat_win.blit(main_text,(160,0))

import pygame
pygame.font.init()

class Text:
    def __init__(self, text, font="Arial",  size=20, color=(0,0,0), isBold=False, background=None):
        self.font = font
        self.size = size
        self.text = text
        self.color = color
        self.isBold = isBold
        self.background = background

    def blit(self, win, x, y):
        text = pygame.font.SysFont(self.font, self.size, self.isBold)
        text = text.render(self.text, True, self.color, self.background)
        win.blit(text, (x, y))