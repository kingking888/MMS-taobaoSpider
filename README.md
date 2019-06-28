# MMS-taobao-Spider 19.6.28
爬取淘宝商品信息 v1.0
## !注意：本项目只为学习交流使用，如有侵犯请联系我立即删除

#### 爬取内容
* 宝贝标题
* 宝贝url
* 宝贝价格
* 宝贝销量
* 店铺名字
* 店铺地址

### 主要python库
* selenium
* pymongo

### 运行环境
* python3.7
* chromedriver
* windows 10

### 前言：  
淘宝反爬虫现在做的比较厉害了，浏览商品的时候会让你登陆，我们最好先登陆进去再进行爬取  
淘宝登入的界面有检测，一旦检查到你搜索了它的网页结构，哪怕是你手动划滚动条都会失败  
我这里采用的是pyautogui来模拟鼠标点击，并且拉取滚动条，一般是可以通过滚动验证的
但是同一个账号登入多了就会失败，手动滚也不行
所以我还是建议使用微博账户登入，登入进去后淘宝基本就没什么限制了，用力爬就行


### 后记：
本来想爬取商品评论的，奈何获取json的接口太复杂了，完全不知道这个ua是什么东西，怎么生成的

![淘宝评论接口](https://github.com/MenMensAa/MMS-taobaoSpider/blob/master/img/%E6%B7%98%E5%AE%9D%E8%AF%84%E8%AE%BA.png)


最后贴一张爬下来的内容


![爬取内容](https://github.com/MenMensAa/MMS-taobaoSpider/blob/master/img/%E6%95%B0%E6%8D%AE%E5%BA%93%E6%88%AA%E5%9B%BE.jpg)
