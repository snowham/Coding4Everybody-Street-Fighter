import reference
import pygame
import sys
sys.path.append('/home/runner/Coding4EverybodyGame/classes')
import entityPlayer
import registry
pygame.init()

pygame.display.set_caption("Coding4Everybody - Street Fighter")
screen = pygame.display.set_mode((reference.WIDTH, reference.HEIGHT))
reference.SCREEN = screen
clock = pygame.time.Clock()
BACKGROUND = reference.BACKGROUND.convert()

player1 = entityPlayer.EntityPlayer([20, reference.GROUND_LEVEL], reference.F1_RIGHT, 'r', 1, [reference.F1_RIGHT, reference.F1_LEFT, reference.L1_PUNCH, reference.R1_PUNCH])
player2 = entityPlayer.EntityPlayer([reference.WIDTH - 120, reference.GROUND_LEVEL], reference.F2_LEFT, 'l', 2, [reference.F2_RIGHT, reference.F2_LEFT, reference.L2_PUNCH, reference.R2_PUNCH])

registry.Registry.register_entity(player1)
registry.Registry.register_entity(player2)



while True:

    # keep the loop running at the right speed
    clock.tick(reference.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            player1.keyDownEvent(event)
            player2.keyDownEvent(event)
        elif event.type == pygame.KEYUP:
            player1.keyUpEvent(event)
            player2.keyUpEvent(event)


    screen.blit(BACKGROUND, [0, 0])

    registry.Registry.update_all()

    pygame.display.flip()
