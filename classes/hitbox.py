import pygame
import reference


class Hitbox(object):
    def __init__(self, X1, Y1, X2, Y2, entitySprite):
        if X2 >= X1:
            self.X1 = X1
            self.X2 = X2
        else:
            self.X1 = X2
            self.X2 = X1
        if Y2 >= Y1:
            self.Y1 = Y1
            self.Y2 = Y2
        else:
            self.Y1 = Y2
            self.Y2 = Y1
        self.entity = entitySprite
        self.isAttack = False
        self.color = reference.PURPLE
    
    def setIsAttack(self, isAttack):
        self.isAttack = isAttack
        if isAttack:
            self.color = reference.FUCHSIA
        else:
            self.color = reference.PURPLE

    def getBoundingBox(self):
        trueX1 = self.X1 + self.entity.pos[0]
        trueY1 = self.Y1 + self.entity.pos[1]
        trueX2 = self.X2 + self.entity.pos[0]
        trueY2 = self.Y2 + self.entity.pos[1]
        return trueX1, trueY1, trueX2, trueY2

    def isPointInHitbox(self, x, y):
        X1, Y1, X2, Y2 = self.getBoundingBox()
        return x >= X1 and x <= X2 and y >= Y1 and y <= Y2

    def isCollidedWith(self, hitbox):
        X1, Y1, X2, Y2 = hitbox.getBoundingBox()
        return self.isPointInHitbox(X1, Y1) or self.isPointInHitbox(X2, Y1) or self.isPointInHitbox(X1, Y2) or self.isPointInHitbox(X2, Y2)

    def draw(self):
        X1, Y1, X2, Y2 = self.getBoundingBox()
        X1 *= reference.WIDTH
        X1 //= 750
        Y1 *= reference.HEIGHT
        Y1 //= 580
        X2 *= reference.WIDTH
        X2 //= 750
        Y2 *= reference.HEIGHT
        Y2 //= 580
        pygame.draw.rect(reference.SCREEN, self.color, (X1, Y1, X2 - X1, Y2 - Y1), 5)