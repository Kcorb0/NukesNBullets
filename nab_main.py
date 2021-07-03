import pygame, sys, os

from pygame.constants import KEYDOWN, KEYUP, K_ESCAPE, K_a, K_d, K_s, K_w

pygame.init()
pygame.font.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('NukesNBullets')
clock = pygame.time.Clock()
scale_mult = 4


player_img = pygame.image.load('images\player\idle\player_idle1.png')
player_img_scaled = pygame.transform.scale(player_img, (player_img.get_width()*scale_mult, player_img.get_height()*scale_mult))

reticle = pygame.image.load('images/reticles/reticle1.png')
reticle_scaled = pygame.transform.scale(reticle, (reticle.get_width()*scale_mult, reticle.get_height()*scale_mult))


class Player:
    def __init__(self, x, y):
        self.player_idle = [scale_img('images\player\idle\player_idle1.png'), scale_img('images\player\idle\player_idle2.png')]
        self.player_walk = [scale_img('images\player\walking\player_walk1.png'), scale_img('images\player\walking\player_walk2.png')]
        self.anim_cnt = 0
        self.image = self.player_idle[self.anim_cnt]
        self.x = x
        self.y = y
        self.vel = 6
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.idle = True
        self.walking = False

    def draw_player(self):
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

        self.anim_cnt += 1
        if self.anim_cnt >= 2:
            self.anim_cnt = 0


def scale_img(img_loc):
    new_img = pygame.image.load(img_loc)
    scaled = pygame.transform.scale(new_img, (new_img.get_width()*scale_mult, new_img.get_height()*scale_mult))
    return scaled


player = Player(WIDTH//2, HEIGHT//2)

while True:
    screen.fill((44, 44, 44))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_w:
                player.up = True
            if event.key == K_s:
                player.down = True
            if event.key == K_a:
                player.left = True
            if event.key == K_d:
                player.right = True
        if event.type == KEYUP:
            if event.key == K_w:
                player.up = False
            if event.key == K_s:
                player.down = False
            if event.key == K_a:
                player.left = False
            if event.key == K_d:
                player.right = False

    player.update_img()
    player.draw_player()
    player.update_img()
    player.update_movement()

    # Blit cursor image that follows the mouse position
    screen.blit(reticle_scaled, [mx-reticle_scaled.get_width()//2, my-reticle_scaled.get_height()//2])
    pygame.display.update()
    clock.tick(60)