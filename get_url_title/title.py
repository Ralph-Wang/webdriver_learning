from selenium import webdriver
from time import sleep
from distutils import log

dr = webdriver.Firefox()

# 输出当前title到命令行
log.warn("before: %s" %(dr.title))
# 访问google
dr.get("http://www.google.com.hk")

# 输出当前title到命令行
log.warn("after: %s" %(dr.title))
sleep(3)
dr.close()
