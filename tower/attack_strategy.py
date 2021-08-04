import math
from abc import ABC, abstractmethod


def in_range(enemy, tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.get_range():
        return True
    return False


"""
syntax: attack_strategy().attack(tower, enemy_group, cd_count)
It's something like you hire a "Strategist" to decide how to attack the enemy
You can add other ways of attack just by expand this module
"""


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        raise NotImplementedError("Please implement this method")


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
                return cd_count
        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():
            if in_range(en, tower):
                en.health -= tower.get_damage()
                cd_count = 0
        return cd_count


class Snipe(AttackStrategy):
    """(Bonus) eliminate an enemy all in once"""
    def attack(self, enemies, tower, cd_count):
        for en in enemies.get():      # see the enemy which are spawned in the map
            if in_range(en, tower):   # if the enemy is in the range of tower 
                en.health = 0         # eliminate the enemy, enemy hp = 0 instantly
                cd_count = 0          # cooldown again
                return cd_count       # return cd_count to make sure other enemies' cooldown for the tower is still not ready
        return cd_count               # which will make sure pcr will only attack one eenmy in a shot
        




