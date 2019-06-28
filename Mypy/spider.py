# 创建一个爬虫对象

import login
import weibo_login
from myException import LittleResultException,NoShopException,NetWorkError
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class taobaoSpider(object):
    def __init__(self, kw):
        '''
        kw存储查询内容，info存储爬取信息
        :param kw:
        '''
        self.kw = kw
        self.info = []

    def collect_info(self, items):
        '''
        收集页面信息
        :param items:传入的每个商品
        '''
        for item in items:
            title = item.find('img', alt=True)['alt']
            item_url = item.find('a', attrs={'trace-price':True})['href']
            price = item.find('strong').text
            number = item.find('div', class_='deal-cnt').text
            location = item.find('div', class_='location').text
            shopName = item.find('div', class_='shop').find('span', class_=False).text
            dic = {
                'shopName': shopName,               #店铺名称
                'title': title,                     #宝贝名字
                'location': location,               #发货地点
                'price': price,                     #价格
                'number': number,                   #销量
                'item_url': 'https' + item_url,     #宝贝链接
            }
            self.info.append(dic)

    def go_to_next_page(self, browser):
        '''
        翻页功能在这里实现，同时检查相关宝贝是否太少，太少则拒绝爬取
        :param browser:
        :return:
        '''
        html = browser.page_source
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        try:
            next_page_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        except:
            raise LittleResultException('与%s相关宝贝太少了没有爬取必要，换个宝贝吧~' % self.kw)
        time.sleep(2)
        content = BeautifulSoup(html, 'lxml')
        items = content.find_all('div', class_='item J_MouserOnverReq')
        self.collect_info(items)
        time.sleep(1)
        next_page_btn.click()
        time.sleep(5)

    def search_kw(self, browser):
        '''
        将kw送入搜索框，如果搜索框加载失败，说明网络环境较差，退出程序
        如果输入的是奇怪的文字，检测到没有相关宝贝后也退出程序
        如果使用淘宝账户login，需要将注释的部分还原
        :param browser:
        :return:
        '''
        try:
            input_box = WebDriverWait(browser, 30).until(EC.presence_of_element_located((
                By.CSS_SELECTOR, '#q')))
            input_box.clear()
            time.sleep(0.5)
            input_box.send_keys(self.kw.strip("'"))
        except:
            raise NetWorkError('当前网络环境较差，请稍后再试')
        time.sleep(2)
        enter = browser.find_element_by_css_selector('#J_TSearchForm > div.search-button > button')
        enter.click()
        # time.sleep(3)
        # handles = browser.window_handles
        # browser.switch_to.window(handles[1])
        sell = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#J_relative > div.sort-row > div > ul > li:nth-child(2) > a')))
        content = BeautifulSoup(browser.page_source, 'lxml')
        error = content.find('li', class_='norestip-title')
        if error:
            raise NoShopException('没有找与%s相关的宝贝，请检查输入是否正确' % self.kw)
        time.sleep(1)
        sell.click()
        time.sleep(3)

    def run(self):
        '''
        爬虫主函数，建议通过微博登入，没有滑动验证，通过淘宝账户登入有概率失败
        :return:
        '''
        browser = weibo_login.__login__()
        # browser = login.__login__()
        time.sleep(2)
        self.search_kw(browser)
        for i in range(5):
            self.go_to_next_page(browser)
        browser.quit()

    def get_info(self):
        '''
        :return:返回爬取信息
        '''
        return self.info
