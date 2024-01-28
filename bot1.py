
from player import *
import math


class Bot1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.all_sprite = None
        self.speedx = None
        self.image = bot1_img
        self.radius = 10
        self.rect = self.image.get_rect()
        self.rect.center = 300, 395
        self.last_update = pg.time.get_ticks()

    def update(self, player:Player, speed):
        player_x = player.rect.x
        player_y = player.rect.y

        Bot1_x = self.rect.x
        Bot1_y = self.rect.y
        distance = ((player_x - Bot1_x) * 2 + (player_y - Bot1_y) * 2) * 0.5
        if distance > -100000:
            angle = math.atan2(player_y - Bot1_y, player_x - Bot1_x)
            Bot1_x += speed * math.cos(angle)
            Bot1_y += speed * math.sin(angle)
            self.rect.x = Bot1_x
            self.rect.y = Bot1_y

    def reset(self):
        pass

