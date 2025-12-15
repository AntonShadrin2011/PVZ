import arcade


class Plants(arcade.Sprite):
    def __init__(self,vid,center_x, center_y , price, hp):
        super().__init__(vid)
        self.center_x = center_x
        self.center_y = center_y
        self.price = price
        self.hp = hp




class Podsolnyx(Plants):
    def __init__(self,center_x, center_y  ):
        super().__init__(vid = 'graphics/Plants/SunFlower/SunFlower_0.png' , center_x = center_x, center_y = center_y, price = 50, hp= 100)

class Orex(Plants):
    def __init__(self,center_x, center_y  ):
        super().__init__(vid = 'graphics/Plants/WallNut/WallNut/WallNut_0.png' , center_x = center_x, center_y = center_y, price = 75, hp= 700)

class Goroxostrel(Plants):
    def __init__(self,center_x, center_y  ):
        super().__init__(vid = 'graphics/Plants/Peashooter/Peashooter_0.png' , center_x = center_x, center_y = center_y, price = 100, hp= 200)