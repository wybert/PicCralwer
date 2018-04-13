# -*- coding: utf-8 -*-
"""
Created on

@author: happybeetle
"""

# import networkx as nx
# from pymongo import MongoClient
import pandas as pd
import urllib
import random
import datetime
import time
import yaml

'''
抓取网页文件内容，保存到内存
'''
#  获取网页
def get_file(url,COOKIE):

    # cookies =  open(COOKIE).read().strip('\n')
    HEADERS = {"cookie": COOKIE}
    req = urllib.request.Request(url, headers=HEADERS)
    for i in range(1,20):
        try:
            script = urllib.request.urlopen(req,timeout = 12).read()
            break
        except Exception as e:
            pass
#     script = urllib2.urlopen(req,timeout = 12).read()
    return script


'''
保存文件到本地
@path  本地路径
@file_name 文件名
@data 文件内容
'''
def save_file(path, file_name, data):
    if data == None:
        return

    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()




# @click.command()
# @click.option('--cookie', default = 'cookies', help='这只浏览器的cookie')
# @click.option('--sleep_interval',default = 30, help='设置休眠时间')
# @click.option('--url_list_path', help='要获取图片的URLs文件')
# @click.option('--picdir', help='要保存图片的路径')
# @click.option('--start',default = 0,  help='从上次断开的地方接着运行')


def crawlerPics(cookie, sleep_interval,url_list_path,picdir,start):
    """爬取新浪微博的图片并保存"""

    url_list = pd.read_csv(url_list_path)
    SLEEP_FLAG = 1

    # start =  0
    for k,item in url_list.iterrows():
        if k >= start:
            print(datetime.datetime.now(),k,item["id"],item["mid"],item["url"])
            url = item["url"]
            file_data = get_file(url,cookie)
            # pic_format = url.split(".")[-1]
            # if len(url.split(".")[-1])>5:
            #     pic_format='xxx'

            file_name = url.split('/')[-1]

            print(file_name)
            save_file(picdir, file_name, file_data)

            #设置随机休眠时间
            sleeptime_one = random.randint(sleep_interval-10,sleep_interval+ 10)
            time.sleep(sleeptime_one)





if __name__ == '__main__':

    pars = yaml.load(open('setting.yml'))
    crawlerPics(**pars)









# 一种有 1968877个图片
