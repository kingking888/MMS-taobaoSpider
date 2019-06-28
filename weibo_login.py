# 使用淘宝绑定微博账户登入
# 注意：请在1920*1080分辨率下使用，否则会出现鼠标漂移，具体鼠标位置需要自行调整

from selenium import webdriver
import time
import pyautogui
import random


def swith_to_static():
    '''
    切换至密码登陆
    :return:
    '''
    time.sleep(1)
    pyautogui.click(x=1510, y=310)
    time.sleep(1)


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


def swicth_to_weibo_page():
    '''
    切换至微博登陆界面
    :return:
    '''
    pyautogui.moveTo(x=1248, y=560, duration=0.5)
    pyautogui.click()
    time.sleep(8)
    pyautogui.moveTo(x=1262, y=250, duration=0.3)
    time.sleep(0.5)
    pyautogui.click()


def __login__():
    '''
    函数主体
    :return: 返回一个已经登陆的浏览器
    '''
    pyautogui.PAUSE = 0.2
    user = {'name': 'yourname',
            'pwd': 'yourpwd'}
    taobao_login_url = 'https://login.taobao.com/member/login.jhtml'
    browser = creat_driver()
    browser.get(taobao_login_url)
    swith_to_static()
    swicth_to_weibo_page()
    input_user_name(user['name'])
    pyautogui.press('tab')
    input_user_name(user['pwd'])
    pyautogui.press('enter')
    time.sleep(1)
    return browser
