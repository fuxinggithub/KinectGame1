import pygame

class Boss():
    """自制一个BOSS的类"""
    def __init__(self,screen):
        """初始化BOSS角色"""
        self.screen = screen

        #加载BOSS图像并获取其外接矩形
        self.image = pygame.image.load('images\关底.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将BOSS放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制BOSS"""
        self.screen.blit(self.image,self.rect)