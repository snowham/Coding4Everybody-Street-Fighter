import entity
import reference
import hitbox
import registry
import healthBar


class EntityFighter(entity.EntitySprite):
    def __init__(self, pos, img, direction, index, positions):
        self.fighterIndex = index

        self.pos = pos
        self.img = img
        self.direction = direction

        self.F_RIGHT, self.F_LEFT, self.L_PUNCH, self.R_PUNCH = positions
        
        self.ySpeed = 0
        self.isPunching = False
        self.hitbox = hitbox.Hitbox(reference.FIGHTER_HITBOX_X1, reference.FIGHTER_HITBOX_Y1, reference.FIGHTER_HITBOX_X2, reference.FIGHTER_HITBOX_Y2, self)
        self.attackHitbox = None
        self.maxHealth = 100
        self.health = self.maxHealth
        if index == 1:
            self.healthBar = healthBar.HealthBar(self, reference.HEALTH_BAR_PLAYER_1_START_X, reference.HEALTH_BAR_PLAYER_1_START_Y)
        else:
            self.healthBar = healthBar.HealthBar(self, reference.HEALTH_BAR_PLAYER_2_START_X, reference.HEALTH_BAR_PLAYER_2_START_Y)
        registry.Registry.register_entity(self.healthBar)

        self.punchTimer = - reference.PUNCH_COOLDOWN
        self.hasPunchHit = False

    def jump(self):
        if self.pos[1] >= reference.GROUND_LEVEL:
            self.ySpeed = - reference.JUMP_STRENGTH
    
    def move(self, distance):
        self.pos[0] += distance
        if distance > 0:
            self.direction = 'r'
            if self.isPunching:
                self.img = self.R_PUNCH
            else:
                self.img = self.F_RIGHT
        elif distance < 0:
            self.direction = 'l'
            if self.isPunching:
                self.img = self.L_PUNCH
            else:
                self.img = self.F_LEFT
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] > reference.WIDTH - 106:
            self.pos[0] = reference.WIDTH - 106
            
#Punching Method
    def punch(self):
        if self.punchTimer <= - reference.PUNCH_COOLDOWN:
            self.setPunching(True)
            self.punchTimer = reference.PUNCH_DURATION

    def setPunching(self, isPunching):
        self.isPunching = isPunching
        if isPunching:
            if self.direction == 'r':
                self.img = self.R_PUNCH
                self.attackHitbox = hitbox.Hitbox(80, 20, 150, 40, self)
                self.attackHitbox.setIsAttack(True)
            elif self.direction == 'l':
                self.attackHitbox = hitbox.Hitbox(-50, 20, 20, 40, self)
                self.attackHitbox.setIsAttack(True)
                self.img = self.L_PUNCH
        else:
            self.attackHitbox = None
            if self.direction == 'r':
                self.img = self.F_RIGHT
            if self.direction == 'l':
                self.img = self.F_LEFT
            self.hasPunchHit = False

    def tryAttackFighter(self, hitbox, damage):
        if self.hitbox.isCollidedWith(hitbox):
            self.attackFighter(damage)
            return True
        else:
            return False
    
    def attackFighter(self, damage):
        self.health -= damage
        self.healthBar.refreshHealthBarFromDamage()
        if self.health <= 0:
            self.health = 0
            registry.Registry.deregister_entity(self)
#End of Punching Method
        
    def getDrawPos(self):
        pos = super().getDrawPos()
        drawX = pos[0]
        drawY = pos[1]
        if self.isPunching and self.direction == 'l':
            drawX -= 30
        return [drawX, drawY]

    def update(self):
        super().update()
        if isinstance(self.attackHitbox, hitbox.Hitbox) and not self.hasPunchHit:
            if registry.FighterRegistry.try_attack_all(self.attackHitbox, reference.PUNCH_DAMAGE, self):
                self.hasPunchHit = True
        if self.ySpeed != 0:
            self.pos[1] += self.ySpeed
        if self.pos[1] >= reference.GROUND_LEVEL:
            self.ySpeed = 0
            self.pos[1] = reference.GROUND_LEVEL
        else:
            self.ySpeed += reference.GRAVITY
        if self.punchTimer > - reference.PUNCH_COOLDOWN:
            self.punchTimer -= 1
        if self.punchTimer == 0:
            self.setPunching(False)
        if reference.DRAW_HITBOXES:
          self.hitbox.draw()
          if self.isPunching:
              self.attackHitbox.draw()