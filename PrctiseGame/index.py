import pygame
from setting import Setting
from plane import Plane
import game_function as gf
from pygame.sprite import Group


def run_game():
    """初始化游戏对象"""
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("MyGame")
    plane = Plane(ai_setting,screen)
    zidans = Group()
    
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_setting,screen,plane,zidans)
        #调用飞船的update方法
        plane.update()
        gf.update_zidans(zidans)
        #每次循环时都重绘屏幕并显示可见
        gf.update_screen(ai_setting,screen,plane,zidans)
        

run_game()