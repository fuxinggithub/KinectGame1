import pygame
from settings import Settings
from ship import Ship
from boss import Boss
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard  

def run_game():
    """初始化游戏对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings,screen,"play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    boss = Boss(screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    alien = Alien(ai_settings,screen)
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            #调用飞船的update方法
            ship.update()
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
        #每次循环时都重绘屏幕并显示可见
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        


run_game()
