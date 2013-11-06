import os
from distutils import log

from selenium import webdriver
import selenium.webdriver.support.ui as ui

dr = webdriver.Firefox()

dr.get('file:///%s' % (os.path.abspath('wait.html')) )

# 通过class_name定位到SignIn按钮
signIn = dr.find_element_by_class_name('button')
# 输出SignIn按钮的值
log.warn(signIn.get_attribute('value'))

wait = ui.WebDriverWait(dr, 10, 0.001)
signIn.click()

def waitIt(dr):
	theValue = dr.find_element_by_id('theP').text
	log.warn(theValue)
	return theValue == 'Clicked'

log.warn('wait start')
wait.until(waitIt)
# wait.until(lambda dr:dr.find_element_by_id('theP').text == 'Clicked' )

log.warn('wait end')

dr.close()
