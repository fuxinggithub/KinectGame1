import sys
import pygame
from zidan import Zidan

def check_keydown_events(event,ai_setting,screen,plane,zidans):
    """响应键盘按下"""
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        plane.moving_left = True
    elif event.key == pygame.K_UP:
        plane.moving_up = True
    elif event.key == pygame.K_DOWN:
        plane.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_zidan(ai_setting,screen,plane,zidans)
        
def check_keyup_events(event,plane):
    """响应键盘弹起"""
    if event.key == pygame.K_RIGHT:
         plane.moving_right = False
    elif event.key == pygame.K_LEFT:
         plane.moving_left = False
    elif event.key == pygame.K_UP:
         plane.moving_up = False
    elif event.key == pygame.K_DOWN:
         plane.moving_down = False

def check_events(ai_setting,screen,plane,zidans):
    """响应鼠标和按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_setting,screen,plane,zidans)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,plane)

def update_screen(ai_setting,screen,plane,zidans):
    """更新屏幕上的图像,并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    for zidan in zidans.sprites():
        zidan.draw_zidan()
    plane.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_zidans(zidans):
    """更新子弹的位置并删除已消失的子弹"""
    #更新子弹的位置
    zidans.update()
    #删除已消失的子弹
    for zidan in zidans.copy():
        if zidan.rect.bottom <= 0:
            zidans.remove(zidan)

def fire_zidan(ai_setting,screen,plane,zidans):
    """如果还没有达到限制,就发射一颗子弹"""
    #创建新子弹,并将其加入到编组zidans中
    if len(zidans) < ai_setting.zidan_allowed:
        new_zidan = Zidan(ai_setting,screen,plane)
        zidans.add(new_zidan)
