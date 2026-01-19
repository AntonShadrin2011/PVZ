import arcade

class Solnish(arcade.Sprite):
    def __init__(self,vid,center_x, center_y,tip ):
        super().__init__(vid)
        self.tip = tip
        if self.tip == 1:
            self.change_y = -3.5
        self.center_x = center_x
        self.center_y = center_y


    def update(self):
        self.center_y += self.change_y
        if self.top < 100:
            self.kill()

