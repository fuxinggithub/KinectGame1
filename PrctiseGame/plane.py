import pygame
class Plane():
    """创建飞s的类"""
    def __init__(self,ai_setting,screen):
        """初始化飞船"""
        self.screen = screen
        self.ai_setting = ai_setting
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('D:\pygame\KinectGame1\KinectGame1\PrctiseGame\images\dddd.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        #使飞船不要移动至屏幕外
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_setting.plane_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_setting.plane_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_setting.plane_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.centery += self.ai_setting.plane_speed_factor
        #根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

