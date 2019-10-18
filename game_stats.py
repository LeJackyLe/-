#coding:GBK
class GameStats():
    """������Ϸ��ͳ����Ϣ"""
    
    def __init__(self,ai_settings):
        """��ʼ��ͳ����Ϣ"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # ��Ϸ������ʱ���ڷǻ״̬
        self.game_active = False
        
        # ��ͣ
        self.pause_active = False
        
        # ���κ�����¶���Ӧ��������ߵ÷�
        with open('data\high_score.txt','r') as file_hc:
            high_score_str = file_hc.read()
            self.high_score = int(high_score_str)
        
    def reset_stats(self):
        """��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
