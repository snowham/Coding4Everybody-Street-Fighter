import entity
import reference
import pygame


class HealthBar(entity.EntitySprite):
    def __init__(self, fighter, startX, startY):
        self.fighter = fighter
        self.oldHealth = fighter.health
        self.oldHealthTimer = 0
        self.startX = startX
        self.startY = startY
        self.img = None
    
    def refreshHealthBarFromDamage(self):
        self.oldHealthTimer = reference.HEALTH_BAR_OLD_HEALTH_DELAY

    def draw(self):
        startX = self.startX * reference.WIDTH // 750
        startY = self.startY * reference.HEIGHT // 580
        health_length = self.fighter.health * reference.WIDTH // 750
        old_health = self.oldHealth * reference.WIDTH // 750
        height = reference.HEALTH_BAR_HEIGHT * reference.HEIGHT // 580
        pygame.draw.rect(reference.SCREEN, reference.RED, [startX, startY, health_length * reference.HEALTH_BAR_AMPLIFIER, reference.HEALTH_BAR_HEIGHT])
        pygame.draw.rect(reference.SCREEN, reference.DARK_RED, [self.fighter.health * reference.HEALTH_BAR_AMPLIFIER + self.startX, self.startY, (self.oldHealth - self.fighter.health) * reference.HEALTH_BAR_AMPLIFIER, reference.HEALTH_BAR_HEIGHT])
        pygame.draw.rect(reference.SCREEN, reference.BLACK, [self.oldHealth * reference.HEALTH_BAR_AMPLIFIER + self.startX, self.startY, (self.fighter.maxHealth- self.oldHealth) * reference.HEALTH_BAR_AMPLIFIER, reference.HEALTH_BAR_HEIGHT])
        pygame.draw.rect(reference.SCREEN, reference.BROWN, [self.startX - reference.HEALTH_BAR_BORDER_WIDTH, self.startY - reference.HEALTH_BAR_BORDER_WIDTH, self.fighter.maxHealth * reference.HEALTH_BAR_AMPLIFIER + 2 * reference.HEALTH_BAR_BORDER_WIDTH, reference.HEALTH_BAR_HEIGHT + 2 * reference.HEALTH_BAR_BORDER_WIDTH], reference.HEALTH_BAR_BORDER_WIDTH)

    def update(self):
        super().update()
        if self.oldHealthTimer > 0:
            self.oldHealthTimer -= 1
        elif self.oldHealth >= self.fighter.health:
            self.oldHealth -= reference.HEALTH_BAR_OLD_HEALTH_DECREASE_SPEED
            if self.oldHealth < self.fighter.health:
                self.oldHealth = self.fighter.health
