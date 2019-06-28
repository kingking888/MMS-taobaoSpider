# 使用淘宝账户登入
# 注意：请在1920*1080分辨率下使用，否则会出现鼠标漂移，具体鼠标位置需要自行调整
from selenium import webdriver
import time
import pyautogui
import random


def input_user_name(message):
    '''
    输入字母间隔采用随机
    :param message:
    :return:
    '''
    for word in message:
        num = random.uniform(0,0.05)
        pyautogui.typewrite(message=word, interval=num)


def creat_driver():
    '''
    初始化浏览器，选择以开发者模式启动
    :return:
    '''
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=chrome_option)
    browser.maximize_window()
    return browser


def lets_fuck_scroll():
    '''
    拉取滚动条
    :return:
    '''
    pyautogui.moveTo(x=1230, y=507, duration=0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(x=1530, y=510, duration=0.1)
    # pyautogui.moveTo(x=1533, y=515, duration=0.1)
    pyautogui.mouseUp()
    time.sleep(0.2)


def swith_to_static():
    '''
    切换至密码登陆
    :return:
    '''
    time.sleep(1)
    pyautogui.click(x=1510, y=310)
    time.sleep(1)
    pyautogui.click(x=1356, y=370)
    time.sleep(0.5)


def ready_for_scroll():
    '''
    移动至滚动条左边，准备开始拉取滚动条
    :return:
    '''
    time.sleep(0.5)
    pyautogui.moveTo(x=1360, y=507, duration=0.2)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=1230, y=507, duration=0.2)
    time.sleep(1)


def __login__():
    '''
    主函数
    :return: 返回已经登陆的浏览器
    '''
    pyautogui.PAUSE = 0.2
    user = {'name': 'yourname',
            'pwd': 'yourpwd'}
    taobao_login_url = 'https://login.taobao.com/member/login.jhtml'
    browser = creat_driver()
    browser.get(taobao_login_url)
    swith_to_static()
    input_user_name(user['name'])
    pyautogui.press('tab')
    input_user_name(user['pwd'])
    ready_for_scroll()
    lets_fuck_scroll()
    pyautogui.moveTo(x=1354, y=569, duration=0.3)
    pyautogui.click()
    return browser
