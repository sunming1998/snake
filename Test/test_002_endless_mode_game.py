import pytest
from Base.BaceAction import BaseAction
from Login.Home_Page import Home_Page
import time
base_action = BaseAction()

class TestEndless:
    # def test_001_close_banner(self):
    #     Home_Page().click_close_banner()
    #     time.sleep(3)
    #
    # def test_002_close_banner2(self):
    #     Home_Page().click_close_banner2()
    #     time.sleep(3)
    #
    # def test_003_close_banner3(self):
    #     Home_Page().click_close_banner3()
    #     time.sleep(4)
    #
    # def test_004_close_banner4(self):
    #     Home_Page().click_close_banner4()
    #     time.sleep(4)
    #
    # def test_005_close_banner5(self):
    #     Home_Page().click_close_banner5()
    #     time.sleep(3)
    #
    def test_005_click_endless_game(self):
        Home_Page().click_endless_mode()
        time.sleep(3)

    def test_006_swpie_snake(self):

        while True:
            Home_Page().swipe()
            Home_Page().swipe2()
            Home_Page().swipe3()
            Home_Page().swipe4()

if __name__ == '__main__':
    A = TestEndless()
    A.test_005_click_endless_game()
    A.test_006_swpie_snake()