import pygame
from bullet import Bullet

class Tower:
    def __init__(self, pos, tower_type="basic"):
        self.pos = pos
        self.type = tower_type
        self.level = 1
        self.cooldown = 0

        if tower_type == "basic":
            self.range = 140
            self.damage = 20
            self.fire_rate = 30
            self.splash = 0
            self.color = (100, 150, 255)

        elif tower_type == "sniper":
            self.range = 260
            self.damage = 60
            self.fire_rate = 70
            self.splash = 0
            self.color = (255, 255, 100)

        else:  # splash tower
            self.range = 150
            self.damage = 25
            self.fire_rate = 45
            self.splash = 60
            self.color = (255, 120, 120)

    def upgrade(self):
        self.level += 1
        self.damage += 10
        self.range += 10
        self.fire_rate = max(15, self.fire_rate - 5)
        if self.splash:
            self.splash += 10

    def update(self, enemies, bullets):
        if self.cooldown > 0:
            self.cooldown -= 1
            return

        for enemy in enemies:
            dx = enemy.rect.centerx - self.pos[0]
            dy = enemy.rect.centery - self.pos[1]
            dist = (dx**2 + dy**2) ** 0.5
            if dist <= self.range:
                bullets.add(
                    Bullet(self.pos, enemy, 6, self.damage, self.splash)
                )
                self.cooldown = self.fire_rate
                break

    def draw(self, screen, hover=False):
        pygame.draw.circle(screen, self.color, self.pos, 15)
        if hover:
            pygame.draw.circle(screen, self.color, self.pos, self.range, 1)

