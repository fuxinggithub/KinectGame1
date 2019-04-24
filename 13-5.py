import pygame
import sys
from pygame.sprite import Sprite
from settings import Settings
from random import randint

class Boll(Sprite):
    """表示一个球的类"""
    def __init__(self,ai_settings,screen):
        """初始化小球属性"""
        self.ai_settings = ai_settings
        self.screen = screen

        #加载小球图形
        self.image = pygame.image.load(r'D:\pygame\KinectGame1\KinectGame1\images\rain.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #设置球的随机位置
        self.rect.x = randint(1,1200)

    def blitme(self):
        """在指定位置绘制球"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """小球开始掉落"""
        self.rect.y += self.ai_settings.boll_speed_factor


        
        
class People(Sprite):
    """表示一个人的类"""
    def __init__(self,ai_settings,screen):
        self.ai_settings = ai_settings
        self.screen = screen
    

        #获取小人的图形
        self.image = pygame.image.load(r'D:\pygame\KinectGame1\KinectGame1\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将小人放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #小人的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #小人移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船位置并防止移至屏幕外"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制小人"""
        self.screen.blit(self.image,self.rect)

def run_game():
    """初始化游戏对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("球")
    boll = Boll(ai_settings,screen)
    people = People(ai_settings,screen)

    while True:
        
        check_events(people)
        people.update()
        check_collide(ai_settings,screen,people,boll)
        boll.update()
        
        update_screen(ai_settings,screen,people,boll)
        

def check_keydown_events(event,people):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        people.moving_right = True
    if event.key == pygame.K_LEFT:
        people.moving_left = True

def check_keyup_events(event,people):
    """响应按键弹起"""
    if event.key == pygame.K_RIGHT:
        people.moving_right = False
    if event.key == pygame.K_LEFT:
        people.moving_left = False

def check_events(people):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,people)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,people)
        elif event.type == pygame.QUIT:
            sys.exit()

def check_collide(ai_settings,screen,people,boll):
    """检测碰撞"""
    if pygame.sprite.collide_mask(people,boll):
          boll.rect.x = randint(1,1200)
          boll.rect.y = 50
    elif boll.rect.top > ai_settings.screen_height:
          boll.rect.x = randint(1,1200)
          boll.rect.y = 50
        
def update_screen(ai_settings,screen,people,boll):
    """更新屏幕上的图像"""
    screen.fill(ai_settings.bg_color)
    people.blitme()
    boll.blitme()
    
    pygame.display.flip()


run_game()