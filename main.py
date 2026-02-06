import pygame, sys
from settings import Settings
from enemy import Enemy
from tower import Tower
from game_stats import GameStats
from path import PATH
from menu import draw_menu

pygame.init()
pygame.mixer.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Tower Defense")
font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
hit_sound = pygame.mixer.Sound("sounds/hit.wav")
boss_sound = pygame.mixer.Sound("sounds/boss.wav")

def reset_game():
    return GameStats(settings), [], pygame.sprite.Group(), pygame.sprite.Group()

stats, towers, enemies, bullets = reset_game()
state = "menu"
spawn_timer = 0
enemies_to_spawn = 0

while True:
    if state == "menu":
        draw_menu(screen, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                stats, towers, enemies, bullets = reset_game()
                state = "game"

    elif state == "game":
        screen.fill(settings.bg_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if stats.money >= settings.tower_cost:
                    towers.append(Tower(event.pos))
                    stats.money -= settings.tower_cost

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u and towers:
                    towers[-1].upgrade()

        # Waves
        spawn_timer += 1
        if spawn_timer > 60 and enemies_to_spawn < stats.wave * 5:
            enemies.add(Enemy(settings))
            enemies_to_spawn += 1
            spawn_timer = 0

        if enemies_to_spawn >= stats.wave * 5 and not enemies:
            stats.wave += 1
            enemies_to_spawn = 0
            if stats.wave % 5 == 0:
                enemies.add(Enemy(settings, boss=True))
                boss_sound.play()

        enemies.update()
        bullets.update()

        for bullet in bullets.copy():
            hit = pygame.sprite.spritecollideany(bullet, enemies)
            if hit:
                hit.health -= bullet.damage
                bullets.remove(bullet)
                hit_sound.play()
                if hit.health <= 0:
                    enemies.remove(hit)
                    stats.money += 30
                    stats.score += 10

        for enemy in enemies.copy():
            if enemy.rect.centerx > settings.screen_width:
                enemies.remove(enemy)
                stats.lives -= 1
                if stats.lives <= 0:
                    state = "menu"

        for tower in towers:
            tower.update(enemies, bullets)
            tower.draw(screen)

        enemies.draw(screen)
        bullets.draw(screen)
        for enemy in enemies:
            enemy.draw_health(screen)

        hud = font.render(
            f"Wave:{stats.wave} Money:{stats.money} Lives:{stats.lives} Score:{stats.score}",
            True, (255, 255, 255))
        screen.blit(hud, (10, 10))

        pygame.display.flip()
        clock.tick(60)

