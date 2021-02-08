#!/usr/bin/env python
# coding=utf-8
'''
Author: Shuangchi He / Yulv
Email: yulvchi@qq.com
Date: 2021-02-08 11:36:34
Description: 深大校园网  在线监测 & 网页版自动登录
'''
import re
import requests
import datetime


def Online_or_not(test_web="https://www.baidu.com"):
    try:
        q=requests.get(test_web, timeout=5)
        m=re.search(r'STATUS OK', q.text)
        if m:
        	print('\n网络连接正常 ~')

        	return True

        else:
        	print('\n网络连接异常 ！')

        	return False

    except:
        print('\n断网了 ......')

        return False


def Web_Login(name, password):
  if not Online_or_not(test_web="https://www.baidu.com"):
    print("{} 网络离线，正在重连...\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
		data = {"DDDDD":name, "upass":password, "R1":0, "R6":0, "para":00, "0MKKey":123456}
		try:
			result = requests.post(Web_URL, data=data)
			print("{} 登录成功~\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    except:
			print("{} 登录失败，未连接网线或WIFI等！\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	else:
		print("{} 网络连接正常~\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


Web_URL = "https://drcom.szu.edu.cn/a70.htm"
Web_Login(name=ahhhh , password='23333')
