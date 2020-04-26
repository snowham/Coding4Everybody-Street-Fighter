import reference

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
        return self.pos

    def draw(self):
        reference.SCREEN.blit(self.img, self.getDrawPos())

    def update(self):
        self.draw()

# I enabled the entityPlayer because it is always better to call a method such as player.startPunch() instead of just doing everything in the main class
# I think we need to clean up our main class more. Use it only to create references in the other classes.
# Also, our code should be based around the update method in entities, menaing that jump should only just set the yspeed of a player to some value like -15 and the update method should update the position
# In addition, we should only use the sprite as a rough outline class and it should not have any hard methods
# I also moved entityPlayer to another file to avoid it this file from having too much stuff - Niels
