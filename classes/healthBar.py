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
        startX = self.startX * reference.WIDTH // reference.WIDTH
        startY = self.startY * reference.HEIGHT // reference.HEIGHT
        health_length = self.fighter.health * reference.WIDTH // reference.WIDTH
        old_health = self.oldHealth * reference.WIDTH // reference.WIDTH
        height = reference.HEALTH_BAR_HEIGHT * reference.HEIGHT // reference.HEIGHT
        max_health = self.fighter.maxHealth * reference.WIDTH // reference.WIDTH
        pygame.draw.rect(reference.SCREEN, reference.RED, [startX, startY, health_length * reference.HEALTH_BAR_AMPLIFIER, height])
        pygame.draw.rect(reference.SCREEN, reference.DARK_RED, [health_length * reference.HEALTH_BAR_AMPLIFIER + startX, startY, (old_health - health_length) * reference.HEALTH_BAR_AMPLIFIER, height])
        pygame.draw.rect(reference.SCREEN, reference.BLACK, [old_health * reference.HEALTH_BAR_AMPLIFIER + startX, startY, (max_health - old_health) * reference.HEALTH_BAR_AMPLIFIER, height])
        pygame.draw.rect(reference.SCREEN, reference.BROWN, [startX - reference.HEALTH_BAR_BORDER_WIDTH, startY - reference.HEALTH_BAR_BORDER_WIDTH, max_health * reference.HEALTH_BAR_AMPLIFIER + 2 * reference.HEALTH_BAR_BORDER_WIDTH, height + 2 * reference.HEALTH_BAR_BORDER_WIDTH], reference.HEALTH_BAR_BORDER_WIDTH)

    def update(self):
        super().update()
        if self.oldHealthTimer > 0:
            self.oldHealthTimer -= 1
        elif self.oldHealth >= self.fighter.health:
            self.oldHealth -= reference.HEALTH_BAR_OLD_HEALTH_DECREASE_SPEED
            if self.oldHealth < self.fighter.health:
                self.oldHealth = self.fighter.health
