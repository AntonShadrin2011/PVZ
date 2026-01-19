import time

import arcade

from Solnish import Solnish
from goroshik import Goroshik


class Plants(arcade.Sprite):
    def __init__(self,vid,center_x, center_y , price, hp):
        super().__init__(vid)
        self.center_x = center_x
        self.center_y = center_y
        self.price = price
        self.hp = hp




class Podsolnyx(Plants):
    def __init__(self,center_x, center_y,main_class  ):
        super().__init__(vid = 'graphics/Plants/SunFlower/SunFlower_0.png' , center_x = center_x, center_y = center_y, price = 50, hp= 100)
        self.timer = time.time()
        self.main_class = main_class
    def update(self):
        if time.time() - self.timer >= 1:
            sol = Solnish('graphics/Plants/Sun/Sun_0.png',self.center_x,self.center_y, 2)
            self.timer = time.time()
            self.main_class.solnish_sprite.append(sol)



class Orex(Plants):
    def __init__(self,center_x, center_y  ):
        super().__init__(vid = 'graphics/Plants/WallNut/WallNut/WallNut_0.png' , center_x = center_x, center_y = center_y, price = 50, hp= 700)

class Goroxostrel(Plants):
    def __init__(self,center_x, center_y,main_class  ):
        super().__init__(vid = 'graphics/Plants/Peashooter/Peashooter_0.png' , center_x = center_x, center_y = center_y, price = 100, hp= 200)
        self.timer = time.time()
        self.main_class = main_class
    def update(self):
        if time.time() - self.timer >= 1:
            sol = Goroshik('graphics/Bullets/PeaNormal/PeaNormal_0.png',self.center_x,self.center_y)
            self.timer = time.time()
            self.main_class.goroshik_sprite.append(sol)





class CherryBomb(Plants):
    def __init__(self, center_x, center_y):
        super().__init__('graphics/Plants/CherryBomb/CherryBomb_0.png', price = 150, hp= 200, center_x = center_x, center_y = center_y)

