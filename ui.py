import pygame

class TowerButton:
    def __init__(self, x, y, text, tower_type, cost):
        self.rect = pygame.Rect(x, y, 120, 40)
        self.text = text
        self.tower_type = tower_type
        self.cost = cost

    def draw(self, screen, font, selected):
        color = (0, 200, 0) if selected else (80, 80, 80)
        pygame.draw.rect(screen, color, self.rect)
        txt = font.render(f"{self.text} (${self.cost})", True, (255, 255, 255))
        screen.blit(txt, (self.rect.x + 5, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

