import arcade

from plants import Podsolnyx

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PVZ'


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ryka = None
        self.background = arcade.load_texture('graphics/Items/Background/Background_0.jpg')
        self.background_m = arcade.load_texture('graphics/Screen/ChooserBackground.png')
        self.cards_money = arcade.load_texture('graphics/Cards/card_sunflower.png')
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

        arcade.draw_texture_rectangle(112, 747, self.cards_money.width - 17, height=self.cards_money.height - 17,
                                      texture=self.cards_money)

        arcade.draw_text(str(self.money), 50, 720, arcade.color.GOLD, 20)
        self.plants_sprite.draw()

        if self.ryka is not None:
            self.ryka.draw()



    def on_update(self, delta_time: float):
        pass

    def on_key_press(self, symbol: int, modifiers: int):
        pass

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if y > 715:
            print(x)
            if 88 < x < 134:
                print('f')
                self.ryka = Podsolnyx(x,y)
                self.ryka.alpha = 170

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.ryka is not None:
            self.ryka.center_x = x
            self.ryka.center_y = y

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.ryka is not None:
            self.plants_sprite.append(self.ryka)
            self.ryka.alpha = 255
            self.ryka = None




okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
#okno.setup()
arcade.run()


"""
- Доделать остальные карточки (просто вставить картинки)
- СДелать правильную проверку на нажатие карточек (в он_маус_пресс)
- Брать в руку не только подсолнух, но и другие объекты
- Добавить своё растение в игру (на свой вкус, точно также, как и подсолнух, пишутер и т.щд.)
- Выставить количество денег в правильное место, чтобы было ровненько всё

"""