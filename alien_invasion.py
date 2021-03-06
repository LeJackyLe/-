#coding:GBK
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_fuctions as gf
from game_stats import GameStats
from button import Button
from pause import Pause
from scoreboard import Scoreboard
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    # 创建按钮
    play_button = Button(ai_settings,screen,"Play")
    pause_button = Pause(ai_settings,screen,"Pause")
    
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,pause_button,
            ship,aliens,bullets)
        
        if stats.game_active and not stats.pause_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
            play_button,pause_button)
        
run_game()
