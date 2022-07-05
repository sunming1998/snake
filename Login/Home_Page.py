from Base.BaceAction import BaseAction

class Home_Page:
    base_action = BaseAction()
    close_banner = 'com.wepie.snake:id/event_type_normal_close_bt'
    close_banner2 = 'com.wepie.snake:id/home_clan_view'
    close_banner3 = 'com.wepie.snake:id/event_type_normal_close_bt'
    close_banner4 = 'com.wepie.snake:id/event_type_normal_close_bt'
    close_banner5 = 'com.wepie.snake:id/event_type_normal_close_bt'
    endless_mode = 'com.wepie.snake:id/home_endless_mode_score_tv'
    zb = [0.12,0.69]
    zb2 = [0.05,0.77]
    zb3 = [0.12, 0.9]
    zb4 = [0.18, 0.8]

    def click_close_banner(self):
        self.base_action.clickElement(self.close_banner)

    def click_close_banner2(self):
        self.base_action.clickElement(self.close_banner2)

    def click_close_banner3(self):
        self.base_action.clickElement(self.close_banner3)

    def click_close_banner4(self):
        self.base_action.clickElement(self.close_banner4)

    def click_close_banner5(self):
        self.base_action.clickElement(self.close_banner5)

    def click_endless_mode(self):
        self.base_action.clickElement(self.endless_mode)

    def swipe(self):
        self.base_action.swipe_to(self.zb, self.zb2, duration=0.01)

    def swipe2(self):
        self.base_action.swipe_to(self.zb2, self.zb3, duration=0.01)

    def swipe3(self):
        self.base_action.swipe_to(self.zb3, self.zb4, duration=0.01)

    def swipe4(self):
        self.base_action.swipe_to(self.zb4, self.zb, duration=0.01)
