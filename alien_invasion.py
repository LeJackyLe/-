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
from scoreboard import Scoreboard
from pygame.sprite import Group

def run_game():
    #��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ�����������Ƿ���
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    # ����Play��ť
    play_button = Button(ai_settings,screen,"Play")
    
    # ����һ�ҷɴ���һ���ӵ������һ�������˱���
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    # ����������Ⱥ
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
    #��ʼ��Ϸ����ѭ��
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,
            bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
            play_button)
        
run_game()
