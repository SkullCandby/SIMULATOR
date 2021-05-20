import pygame
#from spritesheet import Spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.UP_KEY, self.DOWN_KEY, self.FACING_LEFT, self.Y, self.X = False, False, False, False, False, False, False
        self.current_image = pygame.transform.scale(pygame.image.load("data\player.png").convert_alpha(), (80, 60))
        self.rect = self.current_image.get_rect().move(0, 0)

        self.velocity = 0

        self.left_border, self.right_border, self.up_border, self.down_border = 800, 1000, 250, 1000
        self.ground_y = 224
        self.coord_x = (self.rect.x + 20) // 68
        self.coord_y = (self.rect.y + 40) // 68
    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.coord_x = (self.rect.x + 20) // 68
        self.coord_y = (self.rect.y + 40) // 68
        self.velocity = 0
        if self.X:
            if self.LEFT_KEY:
                self.velocity = -2
            elif self.RIGHT_KEY:
                self.velocity = 2
            self.rect.x += self.velocity
        if self.Y:
            if self.UP_KEY:
                self.velocity = -2
            elif self.DOWN_KEY:
                self.velocity = 2

            self.rect.y += self.velocity




    def set_state(self):
        self.state = ' idle'
        if self.velocity > 0:
            self.state = 'moving right'
        elif self.velocity < 0:
            self.state = 'moving left'








