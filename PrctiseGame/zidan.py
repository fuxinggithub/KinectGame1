import pygame
from pygame.sprite import Sprite

class Zidan(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self,ai_setting,screen,plane):
        """在飞船所处的位置创建一个子弹对象"""
        super(Zidan,self).__init__()
        self.screen = screen

        #在(0,0)处创建一个表示子弹的矩形,再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_setting.zidan_width,ai_setting.zidan_height)
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        #存储用小数和表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_setting.zidan_color
        self.speed_factor = ai_setting.zidan_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_zidan(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)
