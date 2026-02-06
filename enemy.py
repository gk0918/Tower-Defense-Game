import pygame
from path import PATH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, settings, boss=False):
        super().__init__()
        self.settings = settings
        self.boss = boss

        size = 40 if boss else 30
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 50, 50) if not boss else (200, 0, 200))
        self.rect = self.image.get_rect(center=PATH[0])

        self.health = settings.boss_health if boss else settings.enemy_health
        self.speed = settings.enemy_speed * (0.6 if boss else 1)
        self.path_index = 0

    def update(self):
        if self.path_index < len(PATH) - 1:
            tx, ty = PATH[self.path_index + 1]
            dx, dy = tx - self.rect.centerx, ty - self.rect.centery
            dist = max(1, (dx**2 + dy**2) ** 0.5)
            self.rect.centerx += int(self.speed * dx / dist)
            self.rect.centery += int(self.speed * dy / dist)

            if abs(dx) < 5 and abs(dy) < 5:
                self.path_index += 1

    def draw_health(self, screen):
        ratio = self.health / (self.settings.boss_health if self.boss else self.settings.enemy_health)
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - 6, self.rect.width, 5))
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.rect.x, self.rect.y - 6, self.rect.width * ratio, 5))

