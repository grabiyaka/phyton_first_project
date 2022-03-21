import pygame, controls
from gun import Gun

ScWth = 700
ScHght = 800

def run():
    pygame.init()
    screen = pygame.display.set_mode((ScWth, ScHght))
    pygame.display.set_caption("Space War")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
         

run()

