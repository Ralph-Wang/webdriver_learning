from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

# 访问google
dr.get("http://www.google.com.hk")

sleep(3)
dr.close()
