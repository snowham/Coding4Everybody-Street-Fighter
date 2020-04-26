import entityFighter

class Registry(object):
    entities = []
    pop = 0

    @classmethod
    def register_entity(cls, entity):
        cls.entities.append(entity)
        cls.pop += 1
        if isinstance(entity, entityFighter.EntityFighter):
            FighterRegistry.register_fighter(entity)

    @classmethod
    def deregister_entity(cls, entity):
        cls.entities.remove(entity)
        if isinstance(entity, entityFighter.EntityFighter):
            FighterRegistry.deregister_fighter(entity)

    @classmethod
    def update_all(cls):
        for i in cls.entities:
            i.update()

class FighterRegistry(object):
    fighters = []
    pop = 0

    @classmethod
    def register_fighter(cls, fighter):
        cls.fighters.append(fighter)
        cls.pop += 1
    
    @classmethod
    def deregister_fighter(cls, fighter):
        cls.fighters.remove(fighter)

    @classmethod
    def try_attack_all(cls, hitbox, damage, source):
        punchHit = False
        for fighter in cls.fighters:
            if fighter != source:
                if fighter.tryAttackFighter(hitbox, damage):
                    punchHit = True
        return punchHit