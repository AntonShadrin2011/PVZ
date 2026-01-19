import arcade
import time
import Solnish
from plants import Podsolnyx, Goroxostrel, Orex, CherryBomb
import random

from zombi import Default

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PVZ'


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ryka = None
        self.solnish_sprite = arcade.SpriteList()
        self.goroshik_sprite = arcade.SpriteList()
        self.zombi_sprite = arcade.SpriteList()
        self.timer = time.time()
        self.background = arcade.load_texture('graphics/Items/Background/Background_0.jpg')
        self.background_m = arcade.load_texture('graphics/Screen/ChooserBackground.png')
        self.cards_money = arcade.load_texture('graphics/Cards/card_sunflower.png')

        self.cards_textures = [
            arcade.load_texture('graphics/Cards/card_sunflower.png'),
            arcade.load_texture('graphics/Cards/card_peashooter.png'),
            arcade.load_texture('graphics/Cards/card_wallnut.png'),
            arcade.load_texture('graphics/Cards/card_cherrybomb.png'),
        ]

        self.plants_sprite = arcade.SpriteList()
        self.money = 50
        self.background_sound = None
        self.game_paused = False

    def setup(self):
        self.background_sound = arcade.load_sound("sounds/grasswalk.mp3")
        arcade.play_sound(self.background_sound, looping=True)

    def on_draw(self):
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, height=self.height,
                                      texture=self.background)

        arcade.draw_texture_rectangle(270, 747, self.background_m.width, height=self.background_m.height,
                                      texture=self.background_m)

        card_x_positions = [112, 172, 232, 292]
        for i, texture in enumerate(self.cards_textures):
            arcade.draw_texture_rectangle(
                card_x_positions[i],
                747,
                texture.width - 17,
                height=texture.height - 17,
                texture=texture
            )

        arcade.draw_text(str(self.money), 47, 707, arcade.color.GOLD, 20, anchor_x="center")
        self.plants_sprite.draw()
        self.solnish_sprite.draw()
        self.goroshik_sprite.draw()
        self.zombi_sprite.draw()

        if self.ryka is not None:
            self.ryka.draw()

        if self.game_paused:
            arcade.draw_text("PAUSED", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 72, anchor_x="center", anchor_y="center")

    def on_update(self, delta_time: float):
        if not self.game_paused:
            self.solnish_sprite.update()
            self.plants_sprite.update()
            self.goroshik_sprite.update()
            self.zombi_sprite.update()
            if time.time() - self.timer >= 5:
                sol = Solnish.Solnish('graphics/Plants/Sun/Sun_0.png', random.randint(100, 1600), 870,1)
                self.timer = time.time()
                self.solnish_sprite.append(sol)
            # todo: сделать так, чтобы зомби не спавнились бесконечно, а тут просто создать таймер отдельный (смотреть на строчку 77)
            spisok_coords = [100, 200, 300, 400, 500]   # todo: change coords
            zombi = Default(random.choice(spisok_coords),0)
            self.zombi_sprite.append(zombi)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            self.game_paused = not self.game_paused

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_paused:
            return
        print(x,y)
        for i in self.solnish_sprite:
            if (i. left <= x <= i.right) and (i.bottom <= y <= i.top):
                i.kill()
                self.money += 50
        if y > 715:

            if 88 < x < 134:
                print('f')
                self.ryka = Podsolnyx(x, y,self)
                self.ryka.alpha = 170

            elif 148 < x < 194:
                print('peashooter')

                self.ryka = Goroxostrel(x, y,self)
                self.ryka.alpha = 170

            elif 208 < x < 254:
                print('wallnut')

                self.ryka = Orex(x, y)
                self.ryka.alpha = 170
            elif 266 < x < 312:
                self.ryka = CherryBomb(x,y)
                self.ryka.alpha = 170

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.game_paused:
            return
        if self.ryka is not None:
            self.ryka.center_x = x
            self.ryka.center_y = y


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.game_paused:
            return
        if self.ryka is not None:
            if self.money >= self.ryka.price:
                if 295 < x < 1178 and 44 < y < 681:

                    self.plants_sprite.append(self.ryka)
                    self.ryka.alpha = 255
                    self.money -= self.ryka.price
                    self.ryka = None
                else:
                    self.ryka = None
            else:
                self.ryka = None





okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
arcade.run()

"""
1. Сделать тудушки в апдейте
2. Добавить газонокосилки (спрайтлист + отрисовать + создать класс + вызвать апдейт) + выставить 5 штук слева от поля

"""