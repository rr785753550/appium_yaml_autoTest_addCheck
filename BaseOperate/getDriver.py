# coding: utf-8
import yaml
import os
from appium import webdriver


# 将设备参数和app包名保存在yaml路径下
def read_deviceYaml():
    # path = os.path.join(os.getcwd(), 'deviceYaml/desired_caps.yaml')
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    path = PATH('../common/deviceYaml/desired_caps.yaml')

    file = open(path, 'r', encoding="utf-8")
    fileInfo = file.read()
    file.close()
    data = yaml.load(fileInfo)
    # print(data)
    return data


def appInfo(appName):
    data = read_deviceYaml()
    appInfo = {}
    appInfo['appPackage'] = data[appName]['appPackage']
    appInfo['appActivity'] = data[appName]['appActivity']
    return appInfo


def mdriver(appName):
    data = read_deviceYaml()
    deviceInfo = data['deviceInfo']
    appiumConfig = data['appiumConfig']
    desired_caps = {}
    desired_caps['platformName'] = deviceInfo['platformName']
    desired_caps['platformVersion'] = str(deviceInfo['platformVersion'])
    desired_caps['deviceName'] = deviceInfo['deviceName']
    desired_caps['automationName'] = appiumConfig['automationName']
    desired_caps['noReset'] = appiumConfig['noReset']
    desired_caps['unicodeKeyboard'] = appiumConfig['unicodeKeyboard']
    desired_caps['resetKeyboard'] = appiumConfig['resetKeyboard']
    desired_caps.update(appInfo(appName))     # 将appInfo字典追加到desired_caps字典后
    serviceInfo = data['serviceInfo']
    driver = webdriver.Remote('http://' + str(serviceInfo['ip']) + ':' + str(serviceInfo['port']) + '/wd/hub', desired_caps)
    return driver

