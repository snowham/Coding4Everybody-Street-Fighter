import reference
import pygame


class Entity(object):
    def update(self):
        pass


class EntitySprite(Entity):
    def __init__(self, pos, img, direction):
        self.pos = pos
        self.img = img
        self.direction = direction
        self.isJump = False

    def getDrawPos(self):
        pos = self.pos
        pos[0] *= reference.WIDTH
        pos[0] //= reference.WIDTH
        pos[1] *= reference.HEIGHT
        pos[1] //= reference.HEIGHT
        return self.pos

    def draw(self):
        img = self.img
        sizeX, sizeY = img.get_size()
        img = pygame.transform.scale(img, (sizeX * reference.WIDTH // reference.WIDTH, sizeY * reference.HEIGHT // reference.HEIGHT))
        reference.SCREEN.blit(img, self.getDrawPos())

    def update(self):
        self.draw()
        
