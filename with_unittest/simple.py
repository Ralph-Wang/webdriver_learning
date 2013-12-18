#coding=utf-8

import unittest
import time
import re
from selenium import webdriver

# 从 unittest.TestCase 继承开始书写测试用例
class TestGet(unittest.TestCase):
  # 每一个测试函数开始执行之前, 都会执行这个 setUp 函数
  def setUp(self):
    self.dr = webdriver.Firefox()
    self.base_url = 'http://115.29.162.102:10000/discuz'

  # 测试函数必须以 test 开头
  def test_get(self):
    dr = self.dr
    dr.get(self.base_url + '/')
    # 用原生的断言 验证跳转至 discuz/forum.php 页面
    assert re.search('discuz', dr.current_url)

  # 每个测试函数执行后, 会执行这个 tearDown 函数
  def tearDown(self):
    self.dr.close()

if __name__ == '__main__':
# 运行测试
  unittest.main()
