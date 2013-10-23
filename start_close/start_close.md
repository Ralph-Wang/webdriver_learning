## 启动/关闭浏览器  

firefox.py
---

	from selenium import webdriver  
	from time import sleep  
	
	dr = webdriver.Firefox()  
	# 3秒后关闭浏览器
	sleep(3)  
	dr.close()

chrome.py
---
	
	from selenium import webdriver  
	from time import sleep
	
	dr = webdriver.Chrome()
	# 3秒后关闭浏览器  
	sleep(3)
	dr.close()

ie.py
---

	from selenium import webdriver
	from time import sleep
	
	dr = webdriver.Ie()
	# 3秒后关闭浏览器  
	sleep(3)
	dr.close()

close_or_quit.py
---
	from selenium import webdriver
	import time
	from distutils import log
	
	
	#计时函数
	def timeIt(func):
		def _wrap(*args):
			start = time.time()
			res = func(*args)
			end = time.time()
			log.warn('call `%s` cost: %s', func.__name__, str(end-start))
			return res
		return _wrap
	
	#2秒后用quit关闭并计时
	def closeWithQuit(webdriver):
		quit = timeIt(webdriver.quit)
		time.sleep(2)
		quit()
	
	#2秒后用close关闭并计时
	def closeWithClose(dr):
		close = timeIt(dr.close)
		time.sleep(2)
		close()
	
	def main():
		log.warn('test Firefox')
		dr = webdriver.Firefox()
		closeWithQuit(dr)
		dr = webdriver.Firefox()
		closeWithClose(dr)
	
		log.warn('test IE')
		dr = webdriver.Ie()
		closeWithQuit(dr)
		dr = webdriver.Ie()
		closeWithClose(dr)
	
		log.warn('test Chrome')
		dr = webdriver.Chrome()
		closeWithQuit(dr)
		dr = webdriver.Chrome()
		closeWithClose(dr)
	
	if __name__ == '__main__':
		main()

