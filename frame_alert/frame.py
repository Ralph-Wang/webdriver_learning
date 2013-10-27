import os
from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()
url = "file:///%s" % (os.path.abspath("main.html"))
dr.get(url)
# 显示frame元素
btn1 = dr.find_element_by_xpath("//input[@id='b1']")
btn1.click()

# 先定位到frame元素
fr = dr.find_element_by_xpath("//iframe[@id='i1']")
# 将dr对象指向frame元素
dr.switch_to_frame(fr)
# 在frame中定位元素并操作
text = dr.find_element_by_xpath("//input[@id='t1']")
btn_in_frame = dr.find_element_by_xpath("//input[@id='b1']")
text.send_keys("Selenium Test")
btn_in_frame.click()
# 输出最后显示的文字
p = dr.find_element_by_xpath("//p[@id='p1']")
log.warn(p.text)

# 回到主页面并隐藏frame
dr.switch_to_default_content()
dr.find_element_by_xpath("//input[@id='b2']").click()


sleep(3)
dr.close()
