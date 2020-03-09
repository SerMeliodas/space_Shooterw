import pygame
import sys
import json
from settings import *

class MenuButton(object):
    def __init__(self):
        super(MenuButton,self).__init__()
        self.image = pygame.image.load('assets/menu/restart_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*5,
                                                        self.image.get_height()*4
                                                        ))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
class SaveButton(object):
    def __init__(self):
        super(SaveButton,self).__init__()
        self.image = pygame.image.load('assets/menu/save_button.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*5,
                                                        self.image.get_height()*4
                                                        ))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
class Menu(pygame.sprite.Sprite):
    def __init__(self,window,MenuButton,SaveButton,player,enemys,score):
        super(Menu,self).__init__()
        self.window = window
        self.player = player
        self.SaveButton = SaveButton
        self.MenuButton = MenuButton
        self.enemys = enemys
        self.score = score
        self.MenuButton.rect.centery += self.SaveButton.rect.height + 10
    def save_score(self,player_nick):
        with open('saves/save.json','r') as file:
            json_1 = json.load(file)
        
        with open("saves/save.json",'w') as file:
            try:
                json_1['save'].append({player_nick:{"score":self.score.score}})
            except:
                json_1 = {'save':[{player_nick:{"score":self.score.score}}]}
            file.write(json.dumps(json_1,indent=2,sort_keys=True))
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
                                self.score.score = 0
                                run = False
                            if (event.pos[0] > self.SaveButton.rect[0] and
                                    event.pos[0] < self.SaveButton.rect[0] + self.SaveButton.rect[2] and
                                    event.pos[1] > self.SaveButton.rect[1] and
                                    event.pos[1] < self.SaveButton.rect[1] + self.SaveButton.rect[3]):
                                input_box = pygame.Rect(WIDTH / 2 - 100, HEIGHT /2 - 32,100,32)
                                player_nick = ''
                                color_inactive = pygame.Color('white')
                                color_active = pygame.Color('red')
                                color = color_inactive
                                text1='please enter your name'
                                text2= "in the  field to"
                                text3= 'save your score'
                                font = pygame.font.Font(None, 32)
                                active = False
                                done = False
                                while not done:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            sys.exit()
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            if input_box.collidepoint(event.pos):
                                                active = not active
                                            else:
                                                active = False
                                            color = color_active if active else color_inactive
                                        if event.type == pygame.KEYDOWN:
                                            if active:
                                                if event.key == pygame.K_RETURN:
                                                    self.save_score(player_nick)
                                                    done = True
                                                    self.window.fill((0,0,0))
                                                elif event.key == pygame.K_BACKSPACE:
                                                    player_nick = player_nick[:-1]
                                                else:
                                                    player_nick += event.unicode
                                    self.window.fill((0,0,0))
                                    txt_surface = font.render(player_nick, True, color)
                                    text_1 = font.render(text1,True,(255,255,255))
                                    text_2 = font.render(text2,True,(255,255,255))
                                    text_3 = font.render(text3,True,(255,255,255))
                                    width = max(200, txt_surface.get_width()+10)
                                    input_box.w = width
                                    self.window.blit(text_3,(WIDTH / 2 - 90,input_box.y - (input_box.height + 5)))
                                    self.window.blit(text_2,(WIDTH / 2 - 80,input_box.y - (input_box.height + 30)))
                                    self.window.blit(text_1,(WIDTH / 2 - 120,input_box.y - (input_box.height + 55)))
                                    self.window.blit(txt_surface, (input_box.x+5, input_box.y+5))
                                    pygame.draw.rect(self.window, color, input_box, 2)
                                    pygame.display.update()                      
                self.window.blit(self.MenuButton.image,self.MenuButton.rect)
                self.window.blit(self.SaveButton.image,self.SaveButton.rect)
                pygame.display.update()