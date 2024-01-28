import os
import pygame as pg
import pygame.mixer as mx

setting = {
    "w":600,
    "h":790,
    "title": "PLAYER VS Aliens",
    "fps": 120,
}

game_folder = os.path.dirname(__name__)
media_folder = os.path.join(game_folder, "media")

player_img =pg.image.load(os.path.join(media_folder,"rx580.png"))
bot1_img=pg.image.load(os.path.join(media_folder,"bot1.png"))

background_img = pg.image.load(os.path.join(media_folder,"60.jpg"))

skins = [player_img]




mx.init()
mx.music.load("musica.wav")
mx.music.set_volume(0.5)
mx.music.play(-1)

clock = pg.time.Clock()
