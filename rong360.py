#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import MySQLdb
import requests
import chardet
import detailInfo
import storeData
import bs4
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 获取参数中网页的内容
def get_page(url):
    try:
        response = requests.post(url)
    except Exception, e:
        print e
    return bs4.BeautifulSoup(response.text)


# 获取一共有多少条优惠
def get_num_of_result(url):
    content = get_page(url)
    result_title = content.find("div", {"class": "result-title"}).string.encode("latin1")
    pattern = re.compile(r'.*?(\d+).*')
    total_result = re.findall(pattern, result_title)[0]
    total_result = int(total_result)  # 总的优惠个数
    print total_result
    num_of_page = total_result / 20
    if total_result % 20 != 0:
        num_of_page += 1
    return num_of_page


# get the content of short description page
def get_short_description_page(url):
    content = get_page(url)
    li = content.findAll("li", {"class": "clearfix"})
    for discount in li:
        img = discount.find("img")['src']
        link = 'http://www.rong360.com/' + discount.find("a")['href']
        print(img)
        print(link)
        discount_dict = detailInfo.get_detail_info(link)
        discount_dict['img'] = img
        discount_dict['type'] = ''
        discount_dict['Characteristic'] = ''
        storeData.store_discount(discount_dict)


con = threading.Condition()
area_code = 0

my_url = 'http://www.rong360.com/credit/f-youhui'

# 同时开启20个线程去抓取它
for i in range(1):
    GetPage().start()



