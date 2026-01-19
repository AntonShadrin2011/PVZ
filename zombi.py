import time

import arcade

from Solnish import Solnish
from goroshik import Goroshik


class Zombi(arcade.Sprite):
    def __init__(self,vid, center_y, hp, row):
        super().__init__(vid)
        self.center_y = center_y
        self.left = 1700
        self.hp = hp
        self.row = row
        self.change_x = 1
    def update(self):
        self.center_x -= self.change_x
        if self.hp == 0:
            self.kill()


class Default(Zombi):
    def __init__(self, center_y,row  ):
        super().__init__(vid = 'zombies/OrdinaryZombie/Zombie_0.png' , center_y = center_y, hp= 100, row = row)
        self.timer = time.time()
        self.row = row


