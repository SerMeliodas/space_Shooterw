import sys
import pygame
from settings import *

class PlayButton(object):
    def __init__(self):
        super(PlayButton,self).__init__()
        self.image = pygame.image.load('assets/menu/play_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = (HEIGHT - HEIGHT / 3) -(50 + (self.rect.height * 3) + 5 * 3)
class ExitButton(object):
    def __init__(self):
        super(ExitButton,self).__init__()
        self.image = pygame.image.load('assets/menu/exit_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = (HEIGHT - HEIGHT / 3) - 50
class ScoreButton(object):
    def __init__(self):
        super(ScoreButton,self).__init__()
        self.image = pygame.image.load('assets/menu/score_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = (HEIGHT - HEIGHT / 3) -(50 + (self.rect.height * 2) + 5 * 2)
class SettingsButton(object):
    def __init__(self):
        super(SettingsButton,self).__init__()
        self.image = pygame.image.load('assets/menu/settings_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = (HEIGHT - HEIGHT / 3) -(50 + self.rect.height + 5)
class MainMenu(pygame.sprite.Sprite):
    def __init__(self,window,exit,play,settings,score):
        super(MainMenu,self).__init__()
        self.background = pygame.image.load('assets/background.png')
        self.rect = self.background.get_rect()
        self.enemy = pygame.image.load('assets/enemy.png')
        self.enemy = pygame.transform.rotozoom(self.enemy,-30,5)
        self.enemy_rect = self.enemy.get_rect()
        self.enemy_rect.left = WIDTH - self.enemy.get_width()
        self.main = pygame.image.load('assets/main.png')
        self.main = pygame.transform.rotozoom(self.main,-30,5)
        self.main_rect = self.main.get_rect()
        self.main_rect.bottom = HEIGHT
        self.play = play
        self.score = score
        self.exit = exit
        self.settings = settings
        self.window = window
    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if (event.pos[0] > self.play.rect[0] and
                                event.pos[0] < self.play.rect[0] + self.play.rect[2] and
                                event.pos[1] > self.play.rect[1] and
                                event.pos[1] < self.play.rect[1] + self.play.rect[3]):
                            run = False
                        if (event.pos[0] > self.score.rect[0] and
                                event.pos[0] < self.score.rect[0] + self.score.rect[2] and
                                event.pos[1] > self.score.rect[1] and
                                event.pos[1] < self.score.rect[1] + self.score.rect[3]):
                            run = False
                        if (event.pos[0] > self.exit.rect[0] and
                                event.pos[0] < self.exit.rect[0] + self.exit.rect[2] and
                                event.pos[1] > self.exit.rect[1] and
                                event.pos[1] < self.exit.rect[1] + self.exit.rect[3]):
                            sys.exit()
                        if (event.pos[0] > self.settings.rect[0] and
                                event.pos[0] < self.settings.rect[0] + self.settings.rect[2] and
                                event.pos[1] > self.settings.rect[1] and
                                event.pos[1] < self.settings.rect[1] + self.settings.rect[3]):
                            run = False
            self.window.blit(self.background,self.rect)
            self.window.blit(self.play.image,self.play.rect)
            self.window.blit(self.exit.image,self.exit.rect)
            self.window.blit(self.score.image,self.score.rect)
            self.window.blit(self.settings.image,self.settings.rect)
            self.window.blit(self.enemy,self.enemy_rect)
            self.window.blit(self.main,self.main_rect)
            pygame.display.update()
