import arcade

class Goroshik(arcade.Sprite):
    def __init__(self,vid,center_x, center_y,main_class ):
        super().__init__(vid)
        self.change_x = -3.5
        self.center_x = center_x
        self.center_y = center_y
        self.main_class = main_class

    def update(self):
        self.center_x -= self.change_x
        if self.left > 1700:
            self.kill()

        hit_list = arcade.check_for_collision_with_list(self,self.main_class.zombi_sprite)
        if len(hit_list) > 0:
            self.kill()
            for zomb in hit_list:
                zomb.hp = zomb.hp - 25