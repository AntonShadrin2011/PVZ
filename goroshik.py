import arcade

class Goroshik(arcade.Sprite):
    def __init__(self,vid,center_x, center_y ):
        super().__init__(vid)
        self.change_x = -3.5
        self.center_x = center_x
        self.center_y = center_y


    def update(self):
        self.center_x -= self.change_x
        if self.left > 1700:
            self.kill()