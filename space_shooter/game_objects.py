import pygame
import random
from settings import *
#============Bullet===============
class Bullet(pygame.sprite.Sprite):
    def __init__(self,position):
        super(Bullet,self).__init__()
        self.image = pygame.image.load('assets/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position
    def update(self):
        self.rect.move_ip(0,-(SPEED + 3))
#=============ENEMY==============
class Enemy(pygame.sprite.Sprite):
    spawn_couldown = 1000
    current_couldown = 0
    def __init__(self,bullets,enemys,player):
        super(Enemy,self).__init__()
        self.image = pygame.image.load('assets/enemy.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*2,
                                                        self.image.get_height()*2))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(round(self.image.get_width() / 2),
                                    WIDTH - round(self.image.get_width() / 2))
        self.rect.y = random.randint(-50,-10)
        self.bullets = bullets
        self.enemys = enemys
        self.player = player
        self.health_point = 2
    def update(self):
        self.rect.move_ip(0,SPEED-2)
        self.bullet_enemy_colysion()
        self.health_update()
        self.enemy_player_colision()
    def bullet_enemy_colysion(self):
        for enemy in self.enemys:
            x = enemy.rect.x + enemy.rect.width/3, (enemy.rect.x + enemy.rect.width) - enemy.rect.width / 3
            y = enemy.rect.y + enemy.rect.height
            x1 = enemy.rect.x, enemy.rect.x + enemy.rect.width
            y1 = enemy.rect.y + 5
            for bullet in self.bullets:
                bullet_x = bullet.rect.x + bullet.rect.width / 2
                if bullet_x > x[0] and bullet_x < x[1] and bullet.rect.y < y:
                    self.bullets.remove(bullet)
                    self.health_point -= 1 
                if bullet_x > x1[0] and bullet_x < x1[1] and bullet.rect.y < y1:
                    self.bullets.remove(bullet)
                    self.health_point -= 1 
    def health_update(self):
        for enemy in list(self.enemys):
            if enemy.health_point == 0:
                self.enemys.remove(enemy)
    def enemy_player_colision(self):
        colision = pygame.sprite.spritecollide(self.player,self.enemys,True)
        if colision:
            self.player.health_point -= 1

    @staticmethod
    def spawn(clock,bullets,enemys,player):
        if Enemy.current_couldown <= 0:
            enemys.add(Enemy(bullets,enemys,player))
            Enemy.current_couldown = Enemy.spawn_couldown
        else:
            Enemy.current_couldown -= clock.get_time()

        for enemy in list(enemys):
            if enemy.rect.top > HEIGHT + enemy.rect.height:
                enemys.remove(enemy)
#============Player================
class Player(pygame.sprite.Sprite):
    def __init__(self,window,name,enemys,bullets,clock):
        super(Player,self).__init__()
        self.health_point = 6
        self.font = pygame.font.Font('assets/fonts/main_font.ttf',20)
        self.image = pygame.image.load('assets/main.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect   = self.image.get_rect()
        self.rect.centerx = WIDTH - 100 / 2
        self.rect.y = HEIGHT - self.rect.height
        self.name = name
        self.clock = clock
        self.bullets = bullets
        self.enemys = enemys
        self.score = 0
        self.window = window
        self.shoot_couldown = 480
        self.current_couldown = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.left -= SPEED

        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.right += SPEED

        if keys[pygame.K_w] and self.rect.top > HEIGHT - HEIGHT /3:
            self.rect.top -= SPEED

        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.bottom += SPEED

        self.shooting()
    def shooting(self):
        if self.current_couldown <= 0:
            self.bullets.add(Bullet(self.rect.midtop))
            self.current_couldown = self.shoot_couldown
        else:
            self.current_couldown -= self.clock.get_time()

        for bullet in list(self.bullets):
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
#============HealthBar================
class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super(HealthBar,self).__init__()
        self.image = pygame.image.load('assets/healthbar/healthbar.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))
        self.rect = self.image.get_rect()

class HealthBarBackground(pygame.sprite.Sprite):
    def __init__(self,player):
        super(HealthBarBackground,self).__init__()
        self.image = pygame.image.load('assets/healthbar/healthbar_background.png')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*3,
                                                        self.image.get_height()*3))

        self.rect = self.image.get_rect()
        self.player = player
    def update(self):
        if self.player.health_point == 6:
            self.rect.left = HEALTH_POSITION[0]
        elif self.player.health_point == 5:
             self.rect.left = HEALTH_POSITION[1]
        elif self.player.health_point == 4:
             self.rect.left = HEALTH_POSITION[2]
        elif self.player.health_point == 3:
            self.rect.left = HEALTH_POSITION[3]
        elif self.player.health_point == 2:
            self.rect.left = HEALTH_POSITION[4]
        elif self.player.health_point == 1:
            self.rect.left = HEALTH_POSITION[5]
        elif self.player.health_point == 0:
            self.rect.left = HEALTH_POSITION[6]
#============Background================
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background,self).__init__()
        self.image = pygame.image.load('assets/background.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
    def update(self):
        self.rect.bottom += SPEED
        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = HEIGHT
