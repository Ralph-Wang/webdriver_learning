import os
from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()
url = "file:///%s" % (os.path.abspath("main.html"))
dr.get(url)

# 点击链接,打开新窗口
l = dr.find_element_by_xpath("//body/a")
l.click()

old_handle = dr.current_window_handle
for handle in dr.window_handles:
	if old_handle != handle:
		new_handle = handle
		break

# 切换到新窗口中,点击新窗口中的按钮
dr.switch_to_window(new_handle)
btn = dr.find_element_by_xpath('//input[@id="b1"]')
btn.click()

# 关闭alert
alert = dr.switch_to_alert()
alert.accept()

sleep(3)
dr.close()
# 切回到原页面关闭
dr.switch_to_window(old_handle)
dr.close()
