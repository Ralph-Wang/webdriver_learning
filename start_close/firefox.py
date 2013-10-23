
from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()
# 3秒后关闭浏览器
sleep(3)
dr.close()
