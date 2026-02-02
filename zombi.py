import time

import arcade

from Solnish import Solnish
from anim import Animation
from goroshik import Goroshik


class Zombi(Animation):
    def __init__(self,vid, center_y, hp, row, main_class):
        super().__init__(vid)
        self.ataca = False
        self.center_y = center_y
        self.left = 1700
        self.hp = hp
        self.row = row
        self.change_x = 10
        self.main_class = main_class
    def update(self):
        if not self.ataca:
            self.center_x -= self.change_x
        if self.hp <= 0:
            self.kill()
        hit_list = arcade.check_for_collision_with_list(self, self.main_class.plants_sprite)
        self.ataca = False
        if len(hit_list) > 0:
            for pl in hit_list:
                pl.hp = pl.hp - 25
                self.ataca = True

class Default(Zombi):
    def __init__(self, center_y,row, main_class  ):
        super().__init__(vid = 'zombies/OrdinaryZombie/Zombie_0.png' , center_y = center_y, hp= 100, row = row, main_class=main_class)
        self.timer = time.time()
        self.row = row
        for i in range (22):
            self.append_texture(arcade.load_texture(f'zombies/OrdinaryZombie/Zombie_{i}.png'))

class ZombiKonys(Zombi):
    def __init__(self, center_y,row, main_class  ):
        super().__init__(vid = 'graphics/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_0.png' , center_y = center_y, hp= 125, row = row, main_class=main_class)
        self.timer = time.time()
        self.row = row
        for i in range (21):
            self.append_texture(arcade.load_texture(f'graphics/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_{i}.png'))


class ZombiVedro(Zombi):
    def __init__(self, center_y,row, main_class  ):
        super().__init__(vid = 'graphics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_0.png' , center_y = center_y, hp= 150, row = row, main_class=main_class)
        self.timer = time.time()
        self.row = row
        for i in range (11):
            self.append_texture(arcade.load_texture(f'graphics/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_{i}.png'))
