import pygame

def scale_img(img_loc, flip=False):
    scale_mult = 4
    new_img = pygame.image.load(img_loc)
    scaled = pygame.transform.scale(new_img, (new_img.get_width()*scale_mult, new_img.get_height()*scale_mult))
    if flip == False:
        return scaled
    else:
        return pygame.transform.flip(scaled, True, False)