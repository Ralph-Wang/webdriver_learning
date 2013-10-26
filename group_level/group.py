import os
from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()
url = "file:///%s" % (os.path.abspath("CheckBox.html"))
dr.get(url)

CheckBoxs = dr.find_elements_by_xpath("//div/input[@type='CHECKBOX']")

# 输出共有多少个CheckBox
log.warn("Counts of CheckBox: %d" % len(CheckBoxs))
# 每隔1秒勾选一个CheckBox
for checkbox in CheckBoxs:
	checkbox.click()
	sleep(1)

# 取消勾选第1个元素
CheckBoxs[0].click()


sleep(3)
dr.close()
