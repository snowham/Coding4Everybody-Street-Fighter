import reference
import pygame
import sys
sys.path.append('./classes') # This is the shorthand equivelent of what we had before, but this works universaly. 
import entityPlayer
import registry

def run(screen):
    background = reference.BACKGROUND.convert()
    clock = pygame.time.Clock()

    player1 = entityPlayer.EntityPlayer([20, reference.GROUND_LEVEL], reference.F1_RIGHT, 'r', 1, [reference.F1_RIGHT, reference.F1_LEFT, reference.L1_PUNCH, reference.R1_PUNCH])
    player2 = entityPlayer.EntityPlayer([reference.WIDTH - 120, reference.GROUND_LEVEL], reference.F2_LEFT, 'l', 2, [reference.F2_RIGHT, reference.F2_LEFT, reference.L2_PUNCH, reference.R2_PUNCH])

    registry.Registry.register_entity(player1)
    registry.Registry.register_entity(player2)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reference.quit_game()
            elif event.type == pygame.KEYDOWN:
                player1.keyDownEvent(event)
                player2.keyDownEvent(event)
            elif event.type == pygame.KEYUP:
                player1.keyUpEvent(event)
                player2.keyUpEvent(event)


        screen.blit(background, [0, 0])

        registry.Registry.update_all()

        pygame.display.flip()

        # keep the loop running at the right speed
        clock.tick(reference.FPS)