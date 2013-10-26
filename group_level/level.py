import os
from time import sleep

from selenium import webdriver

dr = webdriver.Firefox()
url = "file:///%s" % (os.path.abspath("CheckBox.html"))
dr.get(url)

div = dr.find_element_by_xpath("//div[@id='div']")
# 通过已定位的div定位第一个CheckBox
checkbox1 = div.find_element_by_tag_name('input')

checkbox1.click()

sleep(3)
dr.close()
