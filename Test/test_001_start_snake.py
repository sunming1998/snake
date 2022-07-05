import pytest
from Base.BaceAction import BaseAction
from Login.Login_By_QQ import LoginByQQ
import time

class TestStartSnake():

    def test_001_start_app(self):
        self.base_action = BaseAction()
        self.base_action.clearApp()
        time.sleep(1)
        self.base_action.start_app()
        time.sleep(4)

    def test_002_click_agree(self):
        LoginByQQ().click_agree()
        time.sleep(10)

    def test_003_click_location(self):
        LoginByQQ().click_location()
        time.sleep(10)

    def test_004_click_agree1(self):
        LoginByQQ().click_agree1()
        time.sleep(15)

    def test_005_login_by_qq(self):
        LoginByQQ().click_login_by_qq()
        time.sleep(5)

    def test_006_agree_with_qq(self):
        LoginByQQ().click_agree2()
        time.sleep(15)

