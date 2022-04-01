import pygame, controls
from gun import Gun
from pygame.sprite import Group

ScWth = 700
ScHght = 800

def run():
    pygame.init()
    screen = pygame.display.set_mode((ScWth, ScHght))
    pygame.display.set_caption("Space War")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, gun, screen, inos, bullets)
        controls.update_bullets(bullets)
        controls.update_inos(inos)
         

run()

