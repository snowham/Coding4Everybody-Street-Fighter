import entityFighter
import pygame

class EntityPlayer(entityFighter.EntityFighter):
    def keyDownEvent(self, event):
        if (event.key == pygame.K_COMMA and self.fighterIndex == 1) or (event.key == pygame.K_x and self.fighterIndex == 2):
            self.punch()
        if (event.key == pygame.K_w and self.fighterIndex == 1) or (event.key == pygame.K_UP and self.fighterIndex == 2):
            self.jump()
    def keyUpEvent(self, event):
        pass
    
    def update(self):
        super().update()
        key = pygame.key.get_pressed()
        if (key[pygame.K_d] and self.fighterIndex == 1) or (key[pygame.K_RIGHT] and self.fighterIndex == 2):
            if not ((key[pygame.K_a] and self.fighterIndex == 1) or (key[pygame.K_LEFT] and self.fighterIndex == 2)):
                self.move(15)
        if (key[pygame.K_a] and self.fighterIndex == 1) or (key[pygame.K_LEFT] and self.fighterIndex == 2):
            if not ((key[pygame.K_d] and self.fighterIndex == 1) or (key[pygame.K_RIGHT] and self.fighterIndex == 2)):
                self.move(-15)