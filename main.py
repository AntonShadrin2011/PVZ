import arcade
from plants import Podsolnyx, Goroxostrel, Orex, CherryBomb
import random

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PVZ'


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ryka = None
        self.solnish_sprite = arcade.SpriteList()
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

        arcade.draw_text(str(self.money), 37, 720, arcade.color.GOLD, 20)
        self.solnish_sprite.draw()
        self.plants_sprite.draw()

        if self.ryka is not None:
            self.ryka.draw()

    def on_update(self, delta_time: float):
        self.solnish_sprite.update()

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x,y)
        if y > 715:

            if 88 < x < 134:
                print('f')
                self.ryka = Podsolnyx(x, y)
                self.ryka.alpha = 170

            elif 148 < x < 194:
                print('peashooter')

                self.ryka = Goroxostrel(x, y)
                self.ryka.alpha = 170

            elif 208 < x < 254:
                print('wallnut')

                self.ryka = Orex(x, y)
                self.ryka.alpha = 170
            elif 266 < x < 312:
                self.ryka = CherryBomb(x,y)
                self.ryka.alpha = 170

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.ryka is not None:
            self.ryka.center_x = x
            self.ryka.center_y = y


    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
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



'''
Выравнить надпись 
Сделать паузу в игре при нажатии на клавишу ( задание по желанию) 
Попробовать сделать зомби в отдельном файле и заставить их идти в сторону наших растений 

'''