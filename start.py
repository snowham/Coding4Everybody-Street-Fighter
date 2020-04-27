import pygame
import reference
import game_loop

def run(screen):
    clock = pygame.time.Clock()
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                reference.quit_game()
                
        screen.fill(reference.WHITE)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = reference.text_objects("Street Fighter", largeText)
        TextRect.center = ((reference.WIDTH/2),(reference.HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        reference.button(screen,
        "Start",
        reference.WIDTH*150//800,
        reference.HEIGHT*450//600,
        reference.WIDTH*100//800,
        reference.HEIGHT*50//600,
        reference.GREEN,
        reference.BRIGHT_GREEN,
        game_loop.run)

        reference.button(screen,
        "Quit",
        reference.WIDTH*550//800,
        reference.HEIGHT*450//600,
        reference.WIDTH*100//800,
        reference.HEIGHT*50//600,
        reference.RED,
        reference.BRIGHT_RED,
        reference.quit_game)

        pygame.display.update()
        clock.tick(reference.FPS)