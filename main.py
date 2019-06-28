# -*- coding: utf-8 -*-
import pymongo
from spider import taobaoSpider


def save_to_mongodb(data, kw):
    '''
    将传入的数据导入本地mongodb数据库中
    :param data:
    :param kw:
    :return:
    '''
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myClient.taobao_shop
    for item in data:
        result = db[kw].insert_one(item)
        # print(result)


def main():
    '''
    获取输入，建立爬虫对象，返回爬取数据
    :return:
    '''
    kw = input('请输入您想要搜索的宝贝：')
    spider = taobaoSpider(kw)
    try:
        spider.run()
        data = spider.get_info()
        save_to_mongodb(data, kw)
        print('成功保存至mongodb数据库中，请查看')
    except BaseException as e:
        print(e)


if __name__ == '__main__':
    main()