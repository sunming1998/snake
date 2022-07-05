from Base.BaceAction import BaseAction
import pytest
import time
class LoginByQQ():
    base_action = BaseAction()
    agree = 'com.wepie.snake:id/dialog_right_btn'
    login_by_qq = 'com.wepie.snake:id/login_qq_btn'
    location = 'com.wepie.snake:id/start_permission_btn'
    agree1 = 'com.android.packageinstaller:id/permission_allow_button'
    agree_with_qq = 'com.tencent.mobileqq:id/fds'

    def click_location(self):
        self.base_action.clickElement(self.location)

    def click_agree(self):
        self.base_action.clickElement(self.agree)

    def click_login_by_qq(self):
        self.base_action.clickElement(self.login_by_qq)

    def click_agree1(self):
        self.base_action.clickElement(self.agree1)

    def click_agree2(self):
        self.base_action.clickElement(self.agree_with_qq)



