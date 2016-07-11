#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import requests
import chardet
import bs4
import re
import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  # 重新加载sys
sys.setdefaultencoding('utf8')  # 调用setdefaultencoding函数


def regular(pattern, s):
    p = compile(r'' + pattern)
    result = re.findall(p, s)
    return result


def get_detail_info(url):
    try:
        response = requests.post(url)
    except:
        print('Fail to crawl')

    soup = bs4.BeautifulSoup(response.text)
    content = soup.encode('latin1')
    print content

    # 找出银行和优惠简介，也就是第一行的信息
    title = soup.find('div', {'class' : 'p1'}).string.encode('latin1').strip()
    pattern = re.compile(r'【(.*?)】')
    bank = re.findall(pattern, title)[0]
    pattern = re.compile(r'【.*?】(.*)')
    summary = re.findall(pattern, title)[0]
    print 'bank: ' + bank
    print 'summary: ' + summary

    # 优惠的进一步描述
    detail = soup.find('p', {'class' : 'p1'}).string.encode('latin1').strip()
    print 'detail: ' + detail

    # 获取活动时间
    p2 = soup.findAll('div', {'class' : 'p2'})
    data = str(p2[0]).encode('latin1')
    p = re.compile('\s+')
    data = re.sub(p, '', data)
    pattern = re.compile(r'span>(.*?)\(')
    begin_time = re.findall(pattern, data)[0]
    pattern = re.compile(r'~(.*?)\(')
    end_time = re.findall(pattern, data)[0]
    print "begin_time: " + begin_time
    print "end_time: " + end_time

    # 获取使用地区
    data = str(p2[1]).encode('latin1')
    p = re.compile('\s+')
    data = re.sub(p, '', data)
    pattern = re.compile(r'span>(.*?)<')
    area = re.findall(pattern, data)[0]
    print "area: " + area

    # 获取活动内容和活动细则
    con_tit = soup.findAll("div", {"class": "con-tit"})
    for content in con_tit:
        string = content.string.encode('latin1')
        if string == '活动内容':
            activities = content.find_next_sibling().findAll("div", {"class": "list-l"})
            for activity in activities:
                activity_name = activity.find("p", {"class": "list-tit"}).string.encode("latin1")
                imgs = activity.findAll("img")
                for img in imgs:
                    print(img["src"])   # 这里可能有多个img，需要处理一下怎么存
                print(activity_name)


get_detail_info('http://www.rong360.com//credit/youhui/890a775334c95f21c9f172a398f86a89')
