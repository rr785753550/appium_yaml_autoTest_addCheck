# coding: utf-8
"""基本操作： 通过id、text、class查找控件"""

import time
import os
import ast
from selenium.webdriver.support.wait import WebDriverWait


class Element:
    """封装appium中关于元素对象的方法"""
    def __init__(self, driver):
        self.driver = driver

    def get_screenshot(self):
        """截图"""
        now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        screenshoot_path = PATH('../results/screenshot/')
        imageFile = screenshoot_path + "/failpic-" + now + ".png"
        # print(imageFile)
        self.driver.get_screenshot_as_file(imageFile)

    def find_id(self, id):
        """通过id方式查找元素"""
        try:
            WebDriverWait(self.driver, 2).until(lambda driver: driver.find_element_by_id(id).is_displayed())
            self.driver.implicitly_wait(2)
            element = self.driver.find_element_by_id(id)
            return element
        except:
            # 添加抓取log log.error('未定位到元素：'+'%s'%(id))
            # print("未定位到元素：", id)
            self.get_screenshot()
            return False

    def find_text(self, text):
        textXpath = "//*[@text='%s']" % text
        try:
            WebDriverWait(self.driver, 2).until(lambda driver: driver.find_element_by_xpath(textXpath).is_displayed())
            self.driver.implicitly_wait(2)
            element = self.driver.find_element_by_xpath(textXpath)
            return element
        except:
            # print("未定位到元素：", text)
            self.get_screenshot()
            return False

    def find_class(self, className):
        """通过class方式查找元素"""
        try:
            WebDriverWait(self.driver, 2).until(
                lambda driver: driver.find_element_by_class_name(className).is_displayed())
            self.driver.implicitly_wait(2)
            element = self.driver.find_element_by_class_name(className)
            return element
        except:
            # print("未定位到元素：", className)
            self.get_screenshot()
            return False

    def find_xpath(self, xpath):
        """通过xpath方式查找元素"""
        try:
            WebDriverWait(self.driver, 2).until(
                lambda driver: driver.find_element_by_xpath(xpath).is_displayed())
            self.driver.implicitly_wait(2)
            element = self.driver.find_element_by_xpath(xpath)
            return element
        except:
            # print("未定位到元素：", xpath)
            self.get_screenshot()
            return False

    def tap_position(self, position):
        """通过tap点击坐标元素，yaml中坐标写法:(x1, y1), (x2, y2)或(x1, x2)"""
        position = position + ','   # 添加此行的目的是为了防止如果position只有一个时，导致无法整体转化为tuple类型
        str_tuple = ast.literal_eval(position)
        print(str_tuple)
        tuple_list = list(str_tuple)
        print(tuple_list)
        tapElement = self.driver.tap(tuple_list, 500)
        return tapElement

    def swipe_position(self, position):
        """通过swipe从(x1, y1)滑动到(x2, y2)，yaml中坐标写法：(x1, y1), (x2, y2)"""
        str_tuple = ast.literal_eval(position)
        # print(str_tuple)
        x1 = str_tuple[0][0]
        y1 = str_tuple[0][1]
        x2 = str_tuple[1][0]
        y2 = str_tuple[1][1]
        # print(x1, y1, x2, y2)
        self.driver.swipe(x1, y1, x2, y2, 500)

    def get_elementRec(self, element):
        """获取元素的Rec数据，即x, y, width, height"""
        elementRect = element.rect
        return elementRect

    def swipeUp_element(self, element):
        """向上滑动元素"""
        elementRect = element.rect
        elementStartX = elementRect['x']
        elementStartY = elementRect['y']
        elementWidth = elementRect['width']
        elementHeight = elementRect['height']
        x1 = elementStartX + elementWidth / 2
        y1 = elementStartY + elementHeight * 0.75
        y2 = elementStartY + elementHeight * 0.25
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeDown_element(self, element):
        """向上滑动元素"""
        elementRect = element.rect
        iconStartX = elementRect['x']
        iconStartY = elementRect['y']
        iconWidth = elementRect['width']
        iconHeight = elementRect['height']
        x1 = iconStartX + iconWidth / 2
        y1 = iconStartY + iconHeight * 0.25
        y2 = iconStartY + iconHeight * 0.75
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def swipeLeft_element(self, element):
        """向左滑动元素"""
        elementRect = element.rect
        iconStartX = elementRect['x']
        iconStartY = elementRect['y']
        iconWidth = elementRect['width']
        iconHeight = elementRect['height']
        x1 = iconStartX + iconWidth * 0.75
        x2 = iconStartX + iconWidth * 0.25
        y1 = iconStartY + iconHeight / 2
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeRight_element(self, element):
        """向右滑动元素"""
        elementRect = element.rect
        iconStartX = elementRect['x']
        iconStartY = elementRect['y']
        iconWidth = elementRect['width']
        iconHeight = elementRect['height']
        x1 = iconStartX + iconWidth * 0.25
        x2 = iconStartX + iconWidth * 0.75
        y1 = iconStartY + iconHeight / 2
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def seekBar_tapLocation(self, element):
        """点击seekBar的中间位置"""
        elementRect = element.rect
        y = elementRect['y'] + elementRect['height'] / 2
        x1 = elementRect['x'] + elementRect['width'] / 2
        # 点击seekBar位置
        self.driver.tap([(x1, y)], 100)



