
import os
from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()
url = "file:///%s" % (os.path.abspath("main.html"))
dr.get(url)

# 处理alert
btn_for_alert = dr.find_element_by_xpath("//input[@id='b3']")
btn_for_alert.click()
alert = dr.switch_to_alert()
# 输出alert信息
log.warn("alert : %s" % alert.text)
alert.accept()

# 处理confirm
btn_for_confirm = dr.find_element_by_xpath("//input[@id='b4']")
btn_for_confirm.click()
confirm = dr.switch_to_alert()
# 输出confirm信息
log.warn("confirm : %s" % confirm.text)
#confirm.dismiss() #点击取消
confirm.accept() #点击确定

# 处理prompt
btn_for_prompt = dr.find_element_by_xpath("//input[@id='b5']")
btn_for_prompt.click()
prompt = dr.switch_to_alert()
prompt.send_keys("Test selenium")
# 输出prompt的提示信息
log.warn("prompt : %s" % prompt.text)
prompt.accept() #点击确定

sleep(3)
dr.close()
