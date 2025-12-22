import arcade

class Solnish(arcade.Sprite):
    def __init__(self,vid,center_x, center_y ):
        super().__init__(vid)
        self.center_x = center_x
        self.center_y = center_y
