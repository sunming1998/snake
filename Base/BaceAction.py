# coding:utf-8

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import logging

from airtest.utils.logger import get_logger
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import os


class BaseAction(object):
    def __init__(self):
        """
        初始化参数
        """
        if not cli_setup():
            # 连接手机
            auto_setup(__file__, logdir=True, devices=["Android:///", ])
        # 获取定位元素的驱动
        self.__poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        logger = get_logger("airtest")
        logger.setLevel(logging.ERROR)
        # 包名
        self.__packge = "com.wepie.snake"
        # 获取屏幕宽度
        self.width = G.DEVICE.display_info['width']
        # 获取屏幕高度
        self.height = G.DEVICE.display_info['height']
        # 安装包路径
        self.__filePath = ""
        self.__keyEvent = keyevent
        self.__setattr = setattr
        self.__quit = quit
        self.__touch = touch



    def start_app(self):
        """
        打开app
        :return:
        """
        start_app(self.__packge)

    def clearApp(self):
        """
        清除App数据
        :return:
        """
        clear_app(self.__packge)

    def kill_app(self):
        """
        杀掉app进程
        :return:
        """
        shell("am force-stop '{}'".format(self.__packge))

    def stopApp(self):
        """
        关闭App
        :return:
        """
        stop_app(self.__packge)

    def install_app(self):
        """
        安装app
        :return:
        """
        install(self.__filePath)

    def unInstall_app(self):
        """
        卸载app
        :return:
        """
        uninstall(self.__packge)

    def findElement(self, feature):
        """
        通过元素特性查找元素
        :param feature: 元素查找方法
        :return: 返回元素
        """
        if "text=" in feature:
            return self.__poco(text=str(feature[6:-1])).wait(timeout=5)
        # text模糊匹配
        if "textMatches=" in feature:
            return self.__poco(textMatches=str(feature[13:-1]))[0].wait(timeout=5)
        return self.__poco(feature).wait(timeout=5)

    def findeElementParent(self, feature):
        """
        通过该元素查找父亲元素
        :param feature:
        :return:
        """
        return self.findElement(feature).parent()

    def findeElementChild(self, feature, childFeature):
        """
        查找子元素
        :param feature:元素特征
        :param childFeature:子元素特征
        :return:
        """
        return self.findElement(feature).offspring(childFeature)

    def findElementChildren(self, feature):
        """
        查找元素的所有子元素
        :param feature:
        :return:
        """
        return self.findElement(feature).child()

    def touchImg(self, imgFile, times=1):
        """
        点击图片元素
        :param imgFile:元素的图片所在路径
        :param times:点击次数
        :return:
        """
        self.__touch(Template(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\images\{}'.format(imgFile)),
                     times=times)

    def clickElement(self, element):
        """
        点击元素
        :param element: 元素
        :return:
        """
        self.findElement(element).click()

    def clickElementLongTime(self, element):
        """
        长按元素
        :param element:
        :return:
        """
        self.findElement(element).long_click(duration=3)


    def clickElementWait(self, element, times=5):
        """
         等待一定时长找到元素后再点击
        :param element:元素
        :param times: 等待最大时长
        :return:
        """
        self.findElement(element).wait(timeout=times).click()


    def set_text(self, element, content):
        """
        向文本框输入内容
        :param element: 元素
        :param content: 需要输入内容
        :return:
        """
        self.findElement(element).set_text(content)


    def get_text(self, element):
        """
        获取文本内容
        :param element:元素
        :return:
        """
        text = self.findElement(element).get_text()
        return text

    def clear_text(self, element):
        """
        清空文本框内容
        :param element: 元素
        :return:
        """
        self.findElement(element).set_text("")

    def isExistsEment(self, element):
        """
        在一定时间内判断元素是否在页面中存在
        :param element:元素
        :return:在超时间内没有找到元素，返回False,若找到返回True
        """
        return self.findElement(element).wait(timeout=5).exists()

    def click_coordinate(self, zb):
        '''

        :param zb:
        :return:
        '''
        real_zb = int(self.width * zb[0]), int(self.height * zb[1])
        self.__touch(real_zb)

    def swipe_to(self, start, end, duration=0.5):
        """
        滑动 从start 滑动到end
        :param start: 初始坐标 参数形式[x,y]
        :param end: 需要滑动到的位置[x,y]
        :param duration:表示滑动时长
        :return:
        """
        self.__poco.swipe(start, end, duration=duration)

    def swipeByDirection(self, coordinate, direction):
        """
        按照一定的方向滑动
        :param coordinate:初始位置坐标
        :param direction:方向 参数为left=[-0.1,0] right = [0.1,0] up = [0,-0.1] down = [0,0.1]
        :return:
        """
        self.__poco.swipe(coordinate, direction=direction)

    def swipe_alongElement(self, element1, element2):
        """
        把元素1拖到元素2的位置
        :param element1:元素1
        :param element2:元素2
        :return:
        """
        self.findElement(element1).drag_to(self.findElement(element2))

    def swipe_alongElementByCoordinate(self, element, vectory, duration=1):
        """
        将某个元素拖到某个坐标
        :param element: 元素
        :param vectory: 坐标(x,y)
        :param duration:滑动时长
        :return:
        """
        self.__poco.swipe(element, vectory, duration=duration)

    def screenshot(self, filename, msg=''):
        '''
        获取当前页面截图
        :return:
        '''
        snapshot(filename=os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r'\ScreenShot\\' + filename, msg=msg)

    def keySearch(self):
        """
        搜索键
        :return:
        """
        self.__keyEvent("KEYCODE_SEARCH")

    def key_back(self):
        """
        返回键
        :return:
        """
        self.__keyEvent("KEYCODE_BACK")

    def keyEnter(self):
        """
        Enter键
        :return:
        """
        self.__keyEvent("KEYCODE_SEARCH")

    def KeyCode(self, name):
        """
        表示键盘上的按键0-9 A-Z
        :param name: 0-9 A-Z
        :return:
        """
        keys = "KEYCODE_" + str(name)
        self.__keyEvent(keys)

    def setattr(self, element, attr, value):
        '''
        :param element:元素任意属性
        :param attr: 修改元素属性的名称
        :param value:修改元素属性的值
        :return:
        '''
        self.__setattr(self.findElement(element), attr, value)

    def quitDriver(self):
        self.__quit()


if __name__ == '__main__':
    A = BaseAction()
    print(A.width, A.height)
