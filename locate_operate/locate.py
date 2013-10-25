import os
from distutils import log

from selenium import webdriver

dr = webdriver.Firefox()

dr.get('file:///%s' % (os.path.abspath('SignIn.html')) )

# 通过id定位到用户名输入框
username = dr.find_element_by_id('login_field')
# 输出用户名输入框的值
log.warn(username.get_attribute('value'))

# 通过name定位到密码输入框
pwd = dr.find_element_by_name('password')
# 输出密码输入框的值
log.warn(pwd.get_attribute('value'))

# 通过class_name定位到SignIn按钮
signIn = dr.find_element_by_class_name('button')
# 输出SignIn按钮的值
log.warn(signIn.get_attribute('value'))

# 通过css_selector定位到用户名输入框
username_by_css = dr.find_element_by_css_selector("input[type='text']")
# 输出用户名输入框的值
log.warn(username_by_css.get_attribute('value'))

# 通过link_text定位到forgot..链接
forgot = dr.find_element_by_link_text('(forgot password)')
# 输出链接地址
log.warn(forgot.get_attribute('href'))

# 通过partial_link_text定位到forgot..链接
forgot_by_p = dr.find_element_by_partial_link_text('forgot')
# 输出链接地址
log.warn(forgot_by_p.get_attribute('href'))

# 通过tag_name定位到大标题
head1 = dr.find_element_by_tag_name('h1')
# 输出标签内文本
log.warn(head1.text)

# 通过xpath定位到用户名的label
username_label= dr.find_element_by_xpath('//*[@id="login"]/form/div[3]/label[1]')
# 输出标签内文本
log.warn(username_label.text)


dr.close()
