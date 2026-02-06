import pygame

def draw_menu(screen, font):
    screen.fill((0, 0, 0))
    title = font.render("TOWER DEFENSE", True, (255, 255, 255))
    start = font.render("Press SPACE to Start", True, (200, 200, 200))
    screen.blit(title, (300, 200))
    screen.blit(start, (300, 260))
    pygame.display.flip()

