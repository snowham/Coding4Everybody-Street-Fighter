import reference
import pygame
import game_loop
import start
import sys
sys.path.append('./Coding4Everybody-Street-Fighter/classes')
import entityPlayer
import registry

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Coding4Everybody - Street Fighter")
    start.run(reference.SCREEN)