import pygame
from Button import Button


class sneaker:
    def __init__(self, x, y, name, price, filename):
        self.x = x
        self.y = y
        self.name = name
        self.price = price
        self.image = pygame.transform.scale(pygame.image.load(filename), (600, 330))
        self.rect = self.image.get_rect()

    def page(self):
        self.rect.move(self.x, self.y)
        self.font = pygame.font.Font(None, 12)
        self.txt = self.font.render(f'price: {self.price}', True, (0, 125, 0))
        self.txt_coords = (self.x + 30, self.y + 20)
        self.buy_btn = Button(self.x + 15, self.y + 40, 15, 10)
        return self.font, self.txt, self.txt_coords, self.buy_btn