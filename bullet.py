import pygame, math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target, speed, damage, splash):
        super().__init__()
        self.image = pygame.Surface((6, 6))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=pos)

        self.target = target
        self.damage = damage
        self.splash = splash

        dx = target.rect.centerx - pos[0]
        dy = target.rect.centery - pos[1]
        angle = math.atan2(dy, dx)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

