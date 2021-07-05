import sys
from scripts.image_setting import scale_img

class Player:
    def __init__(self, x, y):
        self.anim_cnt = 0
        self.image = None
        self.x = x
        self.y = y
        self.vel = 5
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.idle = True

    def draw_player(self, screen):
        screen.blit(self.image, [self.x-self.image.get_width()//2, self.y-self.image.get_height()//2])

    def update_movement(self):
        if self.up == True:
            self.y -= self.vel
        if self.down == True:
            self.y += self.vel
        if self.left == True:
            self.x -= self.vel
        if self.right == True:
            self.x += self.vel

    def update_img(self):
        player_idle = [scale_img('images\player\idle\player_idle1.png'), scale_img('images\player\idle\player_idle2.png')]
        player_walk_r = [scale_img('images\player\walking\player_walk1.png'), scale_img('images\player\walking\player_walk2.png')]
        player_walk_l = [scale_img('images\player\walking\player_walk1.png', True), scale_img('images\player\walking\player_walk2.png', True)]

        if self.anim_cnt <= 20:
            if self.right == True:
                self.image = player_walk_r[0]
            elif self.left == True:
                self.image = player_walk_l[0]
            elif self.up or self.down:
                self.image = player_walk_r[0]
            else:
                self.image = player_idle[0]
        if self.anim_cnt >= 20:
            if self.right == True:
                self.image = player_walk_r[1]
            elif self.left == True:
                self.image = player_walk_l[1]
            elif self.up or self.down:
                self.image = player_walk_r[1]
            else:
                self.image = player_idle[1]
        if self.anim_cnt >= 40:
            self.anim_cnt = 0
        self.anim_cnt += 1