from bot1 import *
import sys
import time

from bot1 import Bot1

pg.init()

screen = pg.display.set_mode((setting['w'], setting['h']))
size = screen
pg.display.set_caption(setting['title'])

font = pg.font.Font(None, 36)

font = pg.font.Font(None, 36)

sfx = pg.mixer.Sound("sfx.wav")

score = 0
max_score=0


button_text = font.render("Играть", True, "white")
button_rect = button_text.get_rect(center=(setting['w'] // 2, setting['h'] // 2 + 50))

all_sprite1 = pg.sprite.Group()
player = Player()
all_sprite1.add(player)

all_sprite = pg.sprite.Group()
bot1: Bot1 = Bot1()
all_sprite.add(bot1)



timer = pg.USEREVENT + 1
pg.time.set_timer(timer, 1000)

NEW_BOT = pg.USEREVENT + 10
pg.time.set_timer(NEW_BOT, 1000)

collidepoint = pg.sprite.collide_rect(player, bot1)
game_started = False
start_screen = True


def remove_bot1_sprites():
    for bot1 in all_sprite.copy():
        if isinstance(bot1, Bot1):
            all_sprite.remove(bot1)

def start_scene():
    screen.blit(background_img, (0, 0))
    screen.blit(text, text_rect)
    pg.draw.rect(screen, "black", button_rect, 2)
    screen.blit(button_text, button_rect)



run = True
start_time = time.time()
while run:
    if start_screen:

        text = font.render(f"рекорд: {max_score}", True, "black")
        text_rect = text.get_rect(center=(setting['w'] // 2, setting['h'] // 2 - 50))
        start_scene()
    clock.tick(setting['fps'])
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button_rect.collidepoint(mouse_pos):
                start_screen = False
                game_started = True
                sfx.play()

        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()

        if game_started:

            if event.type == timer:
                score += 1

            if score > max_score:
                max_score = score

            if event.type == NEW_BOT:
                new_bot = Bot1()
                all_sprite.add(new_bot)

    if game_started:
        screen.blit(background_img, (0, 0))
        score_text = font.render(f"время: {score}", True, "#000000")
        screen.blit(score_text, (10, 10))

        all_sprite1.draw(screen)
        all_sprite1.update()
        all_sprite.update(player, 1)
        all_sprite.draw(screen)



        if event.type == pg.QUIT:
            run = False
            pg.quit()
            sys.exit()


        if game_started:


            if pg.sprite.spritecollide(player, all_sprite, False):


                player.reset()
                remove_bot1_sprites()
                score = 0
                start_screen = True
                game_started = False



        pg.display.flip()

    if game_started:
        pass

pg.quit()