import pygame
from settings import Settings
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

def run_game():
    """初始化游戏对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("漫天星辰")
    xingxing = Xingxing(ai_settings,screen)
    xingxings = Group()
    creat_fleet(ai_settings,screen,xingxings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        update_screen(ai_settings,screen,xingxings)

class Xingxing(Sprite):
    """创建星星的类"""
    def __init__(self,ai_settings,screen):
        """初始化星星"""
        super(Xingxing,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载图像并获取其外接矩形
        self.image = pygame.image.load(r'D:\pygame\KinectGame1\KinectGame1\images\xingxing.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #星星最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储星星的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image,self.rect)

def get_number_xingxing_x(ai_settings,xingxing_width):
    """计算每行可容纳的星星数量"""
    available_space_x = ai_settings.screen_width - 2 * xingxing_width
    number_xingxing_x = int(available_space_x / (2 * xingxing_width))
    return number_xingxing_x

def get_number_rows(ai_settings,xingxing_height):
    """计算星星的行数"""
    available_space_y = (ai_settings.screen_height - (3 * xingxing_height))
    number_rows = int(available_space_y / (2 * xingxing_height))
    return number_rows

def creat_xingxing(ai_settings,screen,xingxings,xingxing_number,row_number):
    """创建一个星星并将其放在当前行"""
    number_rand = randint(1,1200)
    number_rand1 = randint(1,800)
    xingxing = Xingxing(ai_settings,screen)
    xingxing_width = xingxing.rect.width
    #xingxing.x = xingxing_width + 2 * xingxing_width * xingxing_number
    #xingxing.rect.x = xingxing.x
    #xingxing.rect.y = xingxing.rect.height + 2 * xingxing.rect.height * row_number
    xingxing.rect.x = number_rand
    xingxing.rect.y = number_rand1
    xingxings.add(xingxing)

def creat_fleet(ai_settings,screen,xingxings):
    """创建星星阵容"""
    xingxing = Xingxing(ai_settings,screen)
    #number_xingxing_x = get_number_xingxing_x(ai_settings,xingxing.rect.width)
    #number_rows = get_number_rows(ai_settings,xingxing.rect.height)
    number_rand = randint(0,40)
    for row_number in range(8):
        for xingxing_number in range(10):
            creat_xingxing(ai_settings,screen,xingxings,xingxing_number,row_number)

def update_screen(ai_settings,screen,xingxings):
    screen.fill(ai_settings.bg_color)
    xingxings.draw(screen)
    pygame.display.flip()


run_game()