#coding:GBK
import pygame.font

class Pause():
    
    def __init__(self,ai_settings,screen,msg):
        """初始化按钮属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # 设置按钮的尺寸和其他属性
        self.width,self.height = 50,50
        self.button_color = (230,230,230)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,24)
        
        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.x = self.screen_rect.left + 10
        self.rect.y = self.screen_rect.top + 10
        
        # 按钮的标签只需创建一次
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        
        
