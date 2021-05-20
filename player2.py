import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT = False, False, False
        self.current_image = pygame.image.load('data/player.png')
        self.rect = self.current_image.get_rect()
        self.rect.midbottom = (570, 244)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'idle'
        self.left_border, self.right_border = 250, 1150
        self.ground_y = 224
        self.box = pygame.Rect(self.rect.x, self.rect.y, self.rect.w * 2, self.rect.h)
        self.box.center = self.rect.center
        self.passed = False



    def update(self):
        self.velocity = 0
        if self.LEFT_KEY:
            self.velocity = -2
        elif self.RIGHT_KEY:
            self.velocity = 2
        self.rect.x += self.velocity
        if self.velocity == 0 and self.passed:
            self.passed = False
            self.box.center = self.rect.center
        if self.rect.x > 1150 - self.rect.w:
            self.rect.x = 1150 - self.rect.w
        elif self.rect.x < 250:
            self.rect.x = 250
        self.set_state()

        if self.rect.left > self.box.left and self.rect.right < self.box.right :
            pass
        else:
            self.passed = True
            if self.rect.left > self.box.left :
                self.box.left += self.velocity
            elif self.rect.right < self.box.right :
                self.box.left += self.velocity


    def set_state(self):
        self.state = ' idle'
        if self.velocity > 0:
            self.state = 'moving right'
        elif self.velocity < 0:
            self.state = 'moving left'

