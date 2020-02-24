import pygame
import sys
from settings import *

class MenuButton(object):
    def __init__(self):
        super(MenuButton,self).__init__()
        self.image = pygame.image.load('assets/menu/restart_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*5,
                                                        self.image.get_height()*5
                                                                ))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
class Menu(pygame.sprite.Sprite):
    def __init__(self,window,MenuButton,player,enemys):
        super(Menu,self).__init__()
        self.window = window
        self.player = player
        self.MenuButton = MenuButton
        self.enemys = enemys
    def update(self):
        if self.player.health_point <= 0:
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if (event.pos[0] > self.MenuButton.rect[0] and
                                    event.pos[0] < self.MenuButton.rect[0] + self.MenuButton.rect[2] and
                                    event.pos[1] > self.MenuButton.rect[1] and
                                     event.pos[1] < self.MenuButton.rect[1] + self.MenuButton.rect[3]):
                                self.player.rect.bottom = HEIGHT
                                self.enemys.remove(list(self.enemys))
                                self.player.health_point = 6
                                run = False
                self.window.blit(self.MenuButton.image,self.MenuButton.rect)
                pygame.display.update()