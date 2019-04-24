class Setting():
    """游戏的总设置类"""
    def __init__(self):
        """初始化游戏设置"""
        #显示窗口设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞机的移动速度设置
        self.plane_speed_factor = 1.5

        #子弹设置
        self.zidan_speed_factor = 1
        self.zidan_width = 3
        self.zidan_height = 15
        self.zidan_color = (60,60,60)
        self.zidan_allowed = 3