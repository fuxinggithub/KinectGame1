import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from settings import Settings

class Rain(Sprite):
    """一个展示雨滴的类"""
    def __init__(self,ai_settings,screen):
        """初始化雨滴"""
        super(Rain,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        #加载图像并获取其外接矩形
        self.image = pygame.image.load(r'D:\pygame\KinectGame1\KinectGame1\images\rain.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #雨滴最初在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储雨滴的准确位置
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制雨滴"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """开始下雨"""
        self.y += self.ai_settings.rain_speed_factor
        self.rect.y = self.y



def run_game():
    """初始化游戏对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("下雨了")
    rain = Rain(ai_settings,screen)
    rains = Group()
    create_fleet(ai_settings,screen,rains)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        update_rains(ai_settings,screen,rains)
        update_screen(ai_settings,screen,rains)

def get_number_rain_x(ai_settings,rain_width):
    """计算每行可容纳的雨滴数量"""
    available_space_x = ai_settings.screen_width - 2 * rain_width
    number_rain_x = int(available_space_x / (2 * rain_width))
    return number_rain_x

def create_rain(ai_settings,screen,rains,rain_number):
    """创建一个雨滴并将其放在当前行"""
    rain = Rain(ai_settings,screen)
    rain_width = rain.rect.width
    rain.x = rain_width + 2 * rain_width * rain_number
    rain.rect.x = rain.x
    rains.add(rain)

def create_fleet(ai_settings,screen,rains):
    """创建雨滴阵"""
    rain = Rain(ai_settings,screen)
    number_rain_x = get_number_rain_x(ai_settings,rain.rect.width)
    for rain_number in range(number_rain_x):
        create_rain(ai_settings,screen,rains,rain_number)


def update_rains(ai_settings,screen,rains):
    """更新雨滴位置并检查是否位于屏幕边缘"""
    rains.update()
    for rain in rains:
        if rain.rect.top > ai_settings.screen_height:
            rains.remove(rain)
    if rain.rect.top > ai_settings.screen_height:
        create_fleet(ai_settings,screen,rains)

def update_screen(ai_settings,screen,rains):
    """更新屏幕"""
    screen.fill(ai_settings.bg_color)
    rains.draw(screen)
    pygame.display.flip()

run_game()