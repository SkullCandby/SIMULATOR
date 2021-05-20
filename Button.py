import pygame


class Button:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


    def show(self, text=''):
        btn = pygame.Rect(self.x, self.y, self.w, self.h)
        return btn

    def pressed(self, x, y):
        if self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h:
            return True
        return False
