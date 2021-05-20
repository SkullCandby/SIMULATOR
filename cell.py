import pygame

dd = {'road': pygame.image.load('data/road.png'), 'grass': pygame.image.load('data/grass.png')}

dd['nike'] = pygame.image.load('data/store.png')


class Cell:
    def __init__(self, status, x, y):
        self.size = 68
        self.x = x
        self.y = y
        self.status = status
        self.img = pygame.transform.scale(dd[status], (self.size, self.size))
        self.rect = self.img.get_rect().move(x * self.size, y * self.size)






