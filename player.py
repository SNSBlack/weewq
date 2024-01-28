
from setting import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.self = None
        self.speedx = None
        self.image = player_img
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.center = 500, 500
        self.last_update = pg.time.get_ticks()

    def update(self):

        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speedx = -2
        if keystate[pg.K_d]:
            self.speedx = 2
        self.rect.x += self.speedx
        self.speedy = 0
        if keystate[pg.K_s]:
            self.speedy = 2
        if keystate[pg.K_w]:
            self.speedy = -2
        self.rect.y += self.speedy

        if self.rect.x > setting['w'] - 42:
            self.rect.x -= 600
        if self.rect.x < 0:
            self.rect.x += 600
        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.y > setting['h'] - 42:
            self.rect.y -= 790
        if self.rect.y < 0:
            self.rect.y += -790
        if self.rect.top < 0:
            self.rect.top = 0

    def reset(self):
        pass
