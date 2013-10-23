
from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
# 3秒后关闭浏览器
sleep(3)
dr.close()
