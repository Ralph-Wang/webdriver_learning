from selenium import webdriver
from time import sleep
from distutils import log

dr = webdriver.Firefox()

# 输出当前URL到命令行
log.warn("before: %s" %(dr.current_url))
# 访问google
dr.get("http://www.google.com.hk")

# 输出当前URL到命令行
log.warn("after: %s" %(dr.current_url))
sleep(3)
dr.close()
