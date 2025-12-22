import random
import time
import arcade

CELL_W, CELL_H = 60, 60
ROW, COLUMN = 15, 17

SCREEN_WIDTH = CELL_W * COLUMN
SCREEN_HEIGHT = CELL_H * ROW
SCREEN_TITLE = 'BOMBERMAN'

class Animation(arcade.Sprite):

    I = 0
    time = 0

    def update_animation(self, delta_time: float = 1/60):

        # Обновляем время
        self.time += delta_time

        # Проверяем, прошло ли 1 секунда
        if self.time > 0.01:
            self.time = 0

            # Переключаем текстуру
            if self.I == len(self.textures) - 1:
                self.I = 0
            else:
                self.I += 1

            # Применяем текстуру
            self.set_texture(self.I)

class Boost(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic, scale=0.7)
        self.timer = time.time()
        print(self.timer)

    def update(self):
        pass


class Babax(Animation):
    def __init__(self, pic):
        super().__init__(pic)
        self.timer = time.time()
        print(self.timer)
        for i in range(5):
            self.append_texture(arcade.load_texture(f'Flame/Flame_f0{i}.png'))


    def update(self):
        if time.time() - self.timer >= 5:
            self.kill()


class Map(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)
        self.sloman = arcade.load_texture('Blocks/SlomanBlock.png')
        self.live = 200

    def update(self):
        if self.live <= 0:
            self.kill()
        if 0 < self.live < 146:
            self.texture = self.sloman


class Bombery(Animation):
    def __init__(self, pic):
        super().__init__(pic, scale=0.6)
        self.compass = 3
        self.move = False
        self.speed = 7
        self.sanctions = 1
        self.alive = True
        self.left_storn = []
        self.right_storn = []
        self.top_storn = []
        self.bottom_storn = []
        for i in range (8):
            self.bottom_storn.append(arcade.load_texture(f'Bomberman/Front/Bman_F_f0{i}.png'))
            self.top_storn.append(arcade.load_texture(f'Bomberman/Back/Bman_B_f0{i}.png'))
            self.right_storn.append(arcade.load_texture(f'Bomberman/Side/Bman_S_f0{i}.png'))
            self.left_storn.append(arcade.load_texture(f'Bomberman/Side/Bman_S_f0{i}.png', flipped_horizontally=True))
    def update(self, delta_time: float = 1 / 60):
        if not self.alive:
            return

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        self.proverca( okno.nebedroc_sprite)
        self.proverca( okno.bedroc_sprite)
    def proverca(self,sprite_list):
        hit_list = arcade.check_for_collision_with_list(self,sprite_list,)
        if len(hit_list) > 0:
            for block in hit_list:
                if self.right > block.left and self.compass ==2:
                    self.right = block.left

                if self.left < block.right and self.compass ==4:
                    self.left = block.right

                if self.top > block.bottom and self.compass ==1:
                    self.top = block.bottom

                if self.bottom < block.top and self.compass ==3:
                    self.bottom = block.top




class Block(arcade.Sprite):
    def __init__(self, pic):
        super().__init__(pic)


class Bomb(Animation):
    def __init__(self, pic, player):
        super().__init__(pic, scale=0.7)
        self.timer = time.time()
        self.player = player
        print(self.timer)
        for i in range(3):
            self.append_texture(arcade.load_texture(f'Bomb/Bomb_f0{i}.png'))
    def update(self):
        if time.time() - self.timer >= 10:
            self.kill()
            if self.player == 1:
                okno.bomber1_sprite.sanctions += 1
            elif self.player == 2:
                okno.bomber2_sprite.sanctions += 1

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y + 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x - 60
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)

            bax = Babax('Flame/Flame_f00.png')
            bax.center_x = self.center_x + 60
            bax.center_y = self.center_y - 60
            okno.babax_sprite.append(bax)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1 / 1000)
        self.pole = arcade.load_texture('Blocks/BackgroundTile.png')

        self.bomber1_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')
        self.bomber2_sprite = Bombery('Bomberman/Front/Bman_F_f00.png')

        self.coords = [
            [random.randint(0, 4), random.randint(0, 4)],
            [random.randint(5, 9), random.randint(0, 4)],
            [random.randint(10, 14), random.randint(0, 4)],
            [random.randint(15, 16), random.randint(0, 4)],

            [random.randint(0, 4), random.randint(5, 9)],
            [random.randint(5, 9), random.randint(5, 9)],
            [random.randint(10, 14), random.randint(5, 9)],
            [random.randint(15, 16), random.randint(5, 9)],

            [random.randint(0, 4), random.randint(10, 14)],
            [random.randint(5, 9), random.randint(10, 14)],
            [random.randint(10, 14), random.randint(10, 14)],
            [random.randint(15, 16), random.randint(10, 14)],

        ]
        self.bloki = 7

        self.coordsNeBedroc = []
        for y_block in range(3):
            for x_block in range(4):
                block_coords = set()
                x_start = x_block * 5
                x_end = x_start + 4
                y_start = y_block * 5
                y_end = y_start + 4

                while len(block_coords) < self.bloki:
                    new_coord = (random.randint(x_start, x_end), random.randint(y_start, y_end))
                    block_coords.add(new_coord)

                self.coordsNeBedroc.extend([[x, y] for x, y in block_coords])

        self.bomber1_sprite.center_x = CELL_W
        self.bomber1_sprite.center_y = CELL_H
        self.bomber2_sprite.center_x = SCREEN_WIDTH - CELL_W
        self.bomber2_sprite.center_y = SCREEN_HEIGHT - CELL_H

        self.bedroc_sprite = arcade.SpriteList()
        self.nebedroc_sprite = arcade.SpriteList()

        self.bomb1_sprite = arcade.SpriteList()
        self.bomb2_sprite = arcade.SpriteList()

        self.babax_sprite = arcade.SpriteList()

        self.bomb_sprite = arcade.SpriteList()
        self.flame_sprite = arcade.SpriteList()
        self.speed_sprite = arcade.SpriteList()

        self.speed = 5
        self.mousePres = False

        self.bomb_sound = arcade.load_sound("bombpl.mp3")


        self.game_over = False
        self.winner = None
        self.player1_win_texture = arcade.load_texture('win/win1.png')
        self.player2_win_texture = arcade.load_texture('win/win2.png')

    def setup(self):
        for y in range(ROW):
            for x in range(COLUMN):
                block = Map('Blocks/SolidBlock.png')
                block.center_x = x * CELL_W + CELL_W / 2
                block.center_y = y * CELL_H + CELL_H / 2

                if [x, y] in self.coordsNeBedroc:
                    block = Block('Blocks/ExplodableBlock.png')
                    block.center_x = x * CELL_W + CELL_W / 2
                    block.center_y = y * CELL_H + CELL_H / 2
                    self.nebedroc_sprite.append(block)
                if [x, y] in self.coords:
                    random_boost = random.randint(a=1, b=2)
                    if random_boost == 1:
                        boost = Boost('Powerups/BombPowerup.png')
                        boost.center_x = x * CELL_W + CELL_W / 2
                        boost.center_y = y * CELL_H + CELL_H / 2
                        self.bomb_sprite.append(boost)

                    #if random_boost == 2:
                       # boost = Boost('Powerups/FlamePowerup.png')
                       # boost.center_x = x * CELL_W + CELL_W / 2
                       # boost.center_y = y * CELL_H + CELL_H / 2
                       # self.flame_sprite.append(boost)

                    if random_boost == 2:
                        boost = Boost('Powerups/SpeedPowerup.png')
                        boost.center_x = x * CELL_W + CELL_W / 2
                        boost.center_y = y * CELL_H + CELL_H / 2
                        self.speed_sprite.append(boost)

    def on_draw(self):
        self.clear()

        for y in range(ROW):
            for x in range(COLUMN):
                arcade.draw_texture_rectangle(x * CELL_W + CELL_W / 2, y * CELL_H + CELL_H / 2, CELL_W, CELL_H,
                                              texture=self.pole)
        self.nebedroc_sprite.draw()
        self.bedroc_sprite.draw()

        self.bomber1_sprite.draw()
        self.bomber2_sprite.draw()

        self.bomb1_sprite.draw()
        self.bomb2_sprite.draw()

        self.babax_sprite.draw()

        self.bomb_sprite.draw()
        self.flame_sprite.draw()
        self.speed_sprite.draw()

        # arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        # arcade.draw_rectangle_outline(CELL_W * 15 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        # arcade.draw_rectangle_outline(CELL_W * 25 / 2, CELL_H * 5 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        #
        # arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 15 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)
        # arcade.draw_rectangle_outline(CELL_W * 5 / 2, CELL_H * 25 / 2, CELL_W * 5, CELL_H * 5, arcade.color.RED)


        if self.game_over:
            arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT,
                                         (0, 0, 0, 200))

            if self.winner == 1:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                              self.player1_win_texture.width,
                                              self.player1_win_texture.height,
                                              self.player1_win_texture)
            elif self.winner == 2:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                              self.player2_win_texture.width,
                                              self.player2_win_texture.height,
                                              self.player2_win_texture)

    def on_update(self, delta_time: float):
        if self.game_over:
            return

        self.bomber1_sprite.update()
        self.bomber2_sprite.update()

        self.bomber1_sprite.update_animation()
        self.bomber2_sprite.update_animation()

        self.babax_sprite.update_animation()

        self.bomb1_sprite.update_animation(delta_time = 1/1200)
        self.bomb2_sprite.update_animation()

        self.bomb1_sprite.update()
        self.bomb2_sprite.update()

        self.babax_sprite.update()

        self.bedroc_sprite.update()

        self.bomb_sprite.update()
        self.flame_sprite.update()
        self.speed_sprite.update()

        for flame in self.babax_sprite:
            for block in self.nebedroc_sprite:
                if arcade.check_for_collision(flame, block):
                    block.kill()
            for block in self.bedroc_sprite:
                if arcade.check_for_collision(flame, block):
                    block.live -= 1
                    print(block.live)


            if arcade.check_for_collision(flame, self.bomber1_sprite) and self.bomber1_sprite.alive:
                self.bomber1_sprite.alive = False
                self.check_winner()

            if arcade.check_for_collision(flame, self.bomber2_sprite) and self.bomber2_sprite.alive:
                self.bomber2_sprite.alive = False
                self.check_winner()

        for speed_boost in self.speed_sprite:
            if arcade.check_for_collision(self.bomber1_sprite, speed_boost):
                self.bomber1_sprite.speed += 2
                speed_boost.kill()
            if arcade.check_for_collision(self.bomber2_sprite, speed_boost):
                self.bomber2_sprite.speed += 2
                speed_boost.kill()

        for bomb_boost in self.bomb_sprite:
            if arcade.check_for_collision(self.bomber1_sprite, bomb_boost):
                self.bomber1_sprite.sanctions += 1
                bomb_boost.kill()
            if arcade.check_for_collision(self.bomber2_sprite, bomb_boost):
                self.bomber2_sprite.sanctions += 1
                bomb_boost.kill()


    def check_winner(self):
        if not self.bomber1_sprite.alive and not self.bomber2_sprite.alive:
            self.game_over = True
        elif not self.bomber1_sprite.alive:
            self.game_over = True
            self.winner = 2
        elif not self.bomber2_sprite.alive:
            self.game_over = True
            self.winner = 1

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.game_over:
            return

        print(x // 60, y // 60)
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.mousePres = True
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.bedroc_sprite.append(block)

        if button == arcade.MOUSE_BUTTON_RIGHT:
            center_x = x // 60 * CELL_W + CELL_W / 2
            center_y = y // 60 * CELL_H + CELL_H / 2

            for i in range(len(self.bedroc_sprite)):
                if self.bedroc_sprite[i].center_x == center_x and self.bedroc_sprite[i].center_y == center_y:
                    self.bedroc_sprite.remove(self.bedroc_sprite[i])

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.game_over:
            return

        if self.mousePres == True:
            block = Map('Blocks/SolidBlock.png')
            block.center_x = x // 60 * CELL_W + CELL_W / 2
            block.center_y = y // 60 * CELL_H + CELL_H / 2
            self.bedroc_sprite.append(block)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.mousePres = False

    def on_key_press(self, symbol: int, modifiers: int):
        if self.game_over:
            return

        if symbol == arcade.key.W and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_y = self.bomber1_sprite.speed
            self.bomber1_sprite.move = True
            self.bomber1_sprite.compass = 1
            self.bomber1_sprite.textures = self.bomber1_sprite.top_storn
        elif symbol == arcade.key.S and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_y = -self.bomber1_sprite.speed
            self.bomber1_sprite.move = True
            self.bomber1_sprite.compass = 3
            self.bomber1_sprite.textures = self.bomber1_sprite.bottom_storn
        elif symbol == arcade.key.A and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_x = -self.bomber1_sprite.speed
            self.bomber1_sprite.move = True
            self.bomber1_sprite.compass = 4
            self.bomber1_sprite.textures = self.bomber1_sprite.left_storn
        elif symbol == arcade.key.D and self.bomber1_sprite.move == False:
            self.bomber1_sprite.change_x = self.bomber1_sprite.speed
            self.bomber1_sprite.move = True
            self.bomber1_sprite.compass = 2
            self.bomber1_sprite.textures = self.bomber1_sprite.right_storn

        elif symbol == arcade.key.UP and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_y = self.bomber2_sprite.speed
            self.bomber2_sprite.move = True
            self.bomber2_sprite.compass = 1
        elif symbol == arcade.key.DOWN and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_y = -self.bomber2_sprite.speed
            self.bomber2_sprite.move = True
            self.bomber2_sprite.compass = 3
        elif symbol == arcade.key.LEFT and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_x = -self.bomber2_sprite.speed
            self.bomber2_sprite.move = True
            self.bomber2_sprite.compass = 4
        elif symbol == arcade.key.RIGHT and self.bomber2_sprite.move == False:
            self.bomber2_sprite.change_x = self.bomber2_sprite.speed
            self.bomber2_sprite.move = True
            self.bomber2_sprite.compass = 2

        elif symbol == arcade.key.E:
            if self.bomber1_sprite.sanctions >= 1:
                bomb = Bomb('Bomb/Bomb_f02.png', 1)
                bomb.center_x = self.bomber1_sprite.center_x // 60 * CELL_W + CELL_W / 2
                bomb.center_y = self.bomber1_sprite.center_y // 60 * CELL_W + CELL_W / 2
                self.bomb1_sprite.append(bomb)
                self.bomber1_sprite.sanctions -= 1

                arcade.play_sound(self.bomb_sound)

        elif symbol == arcade.key.RCTRL:
            if self.bomber2_sprite.sanctions >= 1:
                bomb = Bomb('Bomb/Bomb_f02.png', 2)
                bomb.center_x = self.bomber2_sprite.center_x // 60 * CELL_W + CELL_W / 2
                bomb.center_y = self.bomber2_sprite.center_y // 60 * CELL_W + CELL_W / 2
                self.bomb2_sprite.append(bomb)

                self.bomber2_sprite.sanctions -= 1

                arcade.play_sound(self.bomb_sound)

    def on_key_release(self, symbol: int, modifiers: int):
        if self.game_over:
            return

        if symbol == arcade.key.W:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.S:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_y = 0
        elif symbol == arcade.key.A:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_x = 0
        elif symbol == arcade.key.D:
            self.bomber1_sprite.move = False
            self.bomber1_sprite.change_x = 0

        elif symbol == arcade.key.UP:
            self.bomber2_sprite.change_y = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.DOWN:
            self.bomber2_sprite.change_y = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.LEFT:
            self.bomber2_sprite.change_x = 0
            self.bomber2_sprite.move = False
        elif symbol == arcade.key.RIGHT:
            self.bomber2_sprite.change_x = 0
            self.bomber2_sprite.move = False


okno = MyGame(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
okno.setup()
arcade.run()