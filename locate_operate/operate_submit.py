from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()

dr.get('http://www.google.com.hk')

# 定位搜索文本框
s = dr.find_element_by_id('lst-ib')
s.send_keys('selenium-webdriver')
s.submit()

sleep(3)
log.warn(dr.title)
sleep(3)
dr.close()
