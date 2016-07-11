#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import MySQLdb
import requests
import chardet
import bs4
import re
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数


class GetPage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global area_code

        # con.acquire()
        # con.notify()
        # con.release()


        try:
            response = requests.post(my_url)
        except:
            print('Fail to crewl')


        # 抓取整个网页
        soup = bs4.BeautifulSoup(response.text)
        hehe = soup.encode('latin1')
        print hehe

        # 解析出总共有多少个优惠和总的优惠页面数量
        result_title = soup.find("div", {"class": "result-title"}).string.encode("latin1")
        pattern = re.compile(r'.*?(\d+).*')
        total_result = re.findall(pattern, result_title)[0]
        total_result = int(total_result)    # 总的优惠个数
        print total_result
        num_of_page = total_result / 20;
        if total_result % 20 != 0:
            num_of_page += 1
        print num_of_page           # 总的优惠页面数量



        li = soup.findAll("li", {"class": "clearfix"})
        for link in li:
            link = link.find("a")['href']
            link = 'http://www.rong360.com/' + link
            print link







con = threading.Condition()
area_code = 0

# my_url = 'http://www.cpooo.com/company/postcode.php'

my_url = 'http://www.rong360.com/credit/f-youhui'

# 同时开启20个线程去抓取它
for i in range(1):
    GetPage().start()



