import pygame, sys, os

from pygame.constants import KEYDOWN, K_ESCAPE

pygame.init()
pygame.font.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('NukesNBullets')
clock = pygame.time.Clock()
scale_mult = 5


player_img = None

reticle = pygame.image.load('images/reticles/reticle1.png')
reticle_scaled = pygame.transform.scale(reticle, (reticle.get_width()*scale_mult, reticle.get_height()*scale_mult))


while True:
    screen.fill((44, 44, 44))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()


    # Blit cursor image that follows the mouse position
    screen.blit(reticle_scaled, [mx-reticle_scaled.get_width()//2, my-reticle_scaled.get_height()//2])

    pygame.display.update()
    clock.tick(60)