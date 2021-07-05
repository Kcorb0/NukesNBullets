import pygame, sys, os
import csv
from pygame.constants import *
from scripts.player import Player

pygame.init()
pygame.font.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('NukesNBullets')
clock = pygame.time.Clock()
scale_mult = 4

reticle = pygame.image.load('images/reticles/reticle1.png')
reticle_scaled = pygame.transform.scale(reticle, (reticle.get_width()*scale_mult, reticle.get_height()*scale_mult))



def update_screen():
    mx, my = pygame.mouse.get_pos()
    screen.fill((44, 44, 44))

    player.update_img()
    player.draw_player(screen)
    player.update_movement()
    screen.blit(reticle_scaled, [mx-reticle_scaled.get_width()//2, my-reticle_scaled.get_height()//2])
    pygame.display.update()


player = Player(WIDTH//2, HEIGHT//2)


while True:

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


    update_screen()
    clock.tick(60)