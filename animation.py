import pygame

class HitEffect:
    def __init__(self, pos):
        self.pos = pos
        self.radius = 5
        self.life = 10

    def update(self):
        self.radius += 3
        self.life -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 150, 0), self.pos, self.radius, 2)

