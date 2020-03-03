from settings import *
import sys
import pygame

from game_objects import Player, Background, Bullet, Enemy, HealthBar, HealthBarBackground
from menu.restart_menu import Menu,MenuButton
from menu.main_menu import MainMenu,PlayButton,ExitButton,ScoreButton,SettingsButton

pygame.init()
window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

bullets = pygame.sprite.Group()
main_objects = pygame.sprite.Group()
enemys = pygame.sprite.Group()
healthbar = pygame.sprite.Group()
restart_menu = pygame.sprite.Group()
main_menu = pygame.sprite.Group()

player = Player(window,'DeminD',enemys,bullets,clock)
background = Background()

pygame.display.set_caption(f'{player.name}')

main_objects.add(background)
main_objects.add(player)
healthbar.add(HealthBarBackground(player))
healthbar.add(HealthBar())
restart_menu.add(Menu(window,MenuButton(),player,enemys))
main_menu.add(MainMenu(window,ExitButton(),PlayButton(),SettingsButton(),ScoreButton()))

if __name__ == '__main__':
    main_menu.update()
    pygame.display.update()
    while True:
        clock.tick(100)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                sys.exit()

        Enemy.spawn(clock,bullets,enemys,player)

        bullets.update()
        enemys.update()
        healthbar.update()
        main_objects.update()

        main_objects.draw(window)
        bullets.draw(window)
        enemys.draw(window)
        healthbar.draw(window)
        restart_menu.update()
        pygame.display.update()
        player.score += 1
