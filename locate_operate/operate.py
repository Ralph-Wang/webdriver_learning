import os
from time import sleep
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()

dr.get('file:///%s' % (os.path.abspath('SignIn.html')) )

# 通过id定位到用户名输入框
username = dr.find_element_by_id('login_field')
username.clear()
username.send_keys('change the username')
# 输出用户名输入框的值
log.warn(username.get_attribute('value'))

# 通过name定位到密码输入框
pwd = dr.find_element_by_name('password')
pwd.clear()
pwd.send_keys('change the pwd')
# 输出密码输入框的值
log.warn(pwd.get_attribute('value'))

# 通过class_name定位到SignIn按钮
signIn = dr.find_element_by_class_name('button')
# 试试clear能否清除按钮的值
# signIn.clear() 不行
# 点击SignIn按钮
signIn.click()
log.warn(signIn.get_attribute('value'))

sleep(5)
dr.close()
