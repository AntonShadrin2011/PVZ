import arcade
import time
import random
import Solnish
from plants import Orex
from zombi import Default, ZombiKonys, ZombiVedro

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'PVZ'


class LawnMower(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__('graphics/Screen/car.png')
        self.center_x = x
        self.center_y = y
        self.active = False
        self.speed = 10
        self.has_been_activated = False

    def update(self):
        if self.active:
            self.center_x += self.speed
            if self.center_x > SCREEN_WIDTH + 100:
                self.active = False




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ryka = None
        self.solnish_sprite = arcade.SpriteList()
        self.goroshik_sprite = arcade.SpriteList()
        self.zombi_sprite = arcade.SpriteList()
        self.timer = time.time()
        self.zombi_timer = time.time()
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
        self.lawn_mowers = arcade.SpriteList()
        self.game_over = False

    def setup(self):
        self.background_sound = arcade.load_sound("sounds/grasswalk.mp3")
        #arcade.play_sound(self.background_sound, looping=True)

        lawn_mower_y_positions = [120, 242, 361, 491, 618]
        for y_pos in lawn_mower_y_positions:
            mower = LawnMower(270, y_pos)
            self.lawn_mowers.append(mower)

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
        self.lawn_mowers.draw()
        for mower in self.lawn_mowers:
            mower.draw()

        if self.ryka is not None:
            self.ryka.draw()

        if self.game_paused:
            arcade.draw_text("PAUSED", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 72, anchor_x="center",
                             anchor_y="center")

        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 72,
                             anchor_x="center",
                             anchor_y="center")

    def on_update(self, delta_time: float):
        if self.game_over or self.game_paused:
            return

        self.solnish_sprite.update_animation()
        self.solnish_sprite.update()
        self.plants_sprite.update()
        self.plants_sprite.update_animation()
        self.goroshik_sprite.update()
        self.zombi_sprite.update()
        self.zombi_sprite.update_animation()

        for mower in self.lawn_mowers:
            mower.update()


        for zombi in self.zombi_sprite:

            if zombi.center_x < 50:
                self.game_over = True
                return


            for mower in self.lawn_mowers:
                hit_list = arcade.check_for_collision_with_list(mower, self.zombi_sprite)
                if len(hit_list) > 0:
                    mower.active = True
                    for zomb in hit_list:
                        zomb.hp = zomb.hp - 1000

        if time.time() - self.timer >= 5:
            sol = Solnish.Solnish('graphics/Plants/Sun/Sun_0.png', random.randint(100, 1600), 870, 1)
            self.timer = time.time()
            self.solnish_sprite.append(sol)

        if time.time() - self.zombi_timer >= 2:
            spisok_coords = [108, 234, 353, 486, 620]
            chislo = random.randint(0, 2)
            zombi = 0
            if chislo == 0:
                zombi = Default(random.choice(spisok_coords), 0, self)
            elif chislo == 1:
                zombi = ZombiKonys(random.choice(spisok_coords), 0, self)
            elif chislo == 2:
                zombi = ZombiVedro(random.choice(spisok_coords), 0, self)
            self.zombi_sprite.append(zombi)
            self.zombi_timer = time.time()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.P:
            self.game_paused = not self.game_paused

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_paused or self.game_over:
            return


        from plants import Podsolnyx, Goroxostrel, Orex, CherryBomb

        print(x, y)
        for i in self.solnish_sprite:
            if (i.left <= x <= i.right) and (i.bottom <= y <= i.top):
                i.kill()
                self.money += 50
        if y > 715:
            if 88 < x < 134:
                print('f')
                self.ryka = Podsolnyx(x, y, self)
                self.ryka.alpha = 170
            elif 148 < x < 194:
                print('peashooter')
                self.ryka = Goroxostrel(x, y, self)
                self.ryka.alpha = 170
            elif 208 < x < 254:
                print('wallnut')
                self.ryka = Orex(x, y)
                self.ryka.alpha = 170
            elif 266 < x < 312:
                self.ryka = CherryBomb(x, y)
                self.ryka.alpha = 170

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.game_paused or self.game_over:
            return
        if self.ryka is not None:
            self.ryka.center_x = x
            self.ryka.center_y = y

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.game_paused or self.game_over:
            return
        if self.ryka is not None:
            if self.money >= self.ryka.price:
                if 295 < x < 1178 and 44 < y < 681:
                    if 295 < x < 405:
                        self.ryka.center_x = 350
                    if 405 < x < 498:
                        self.ryka.center_x = 451.5
                    if 498 < x < 591:
                        self.ryka.center_x = 544.5
                    if 591 < x < 696:
                        self.ryka.center_x = 643.5
                    if 696 < x < 785:
                        self.ryka.center_x = 727
                    if 785 < x < 892:
                        self.ryka.center_x = 838.5
                    if 892 < x < 974:
                        self.ryka.center_x = 933
                    if 974 < x < 1078:
                        self.ryka.center_x = 1026
                    if 1078 < x < 1198:
                        self.ryka.center_x = 1138


                    if 36 < y < 172:
                        self.ryka.center_y = 104
                    if 172 < y < 300:
                        self.ryka.center_y = 236
                    if 300 < y < 438:
                        self.ryka.center_y = 369
                    if 438 < y < 571:
                        self.ryka.center_y = 504
                    if 571 < y < 700:
                        self.ryka.center_y = 636
                    self.plants_sprite.append(self.ryka)
                    self.ryka.alpha = 255
                    self.money -= self.ryka.price
                    self.ryka = None
                else:
                    self.ryka = None
            else:
                self.ryka = None


okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
okno.setup()
arcade.run()