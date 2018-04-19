# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
class Test(unittest.TestCase):  # 起一个类的名称
    '''Test脚本用例'''
# setUp是每个def的开始，tearDown是每个def的结束
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    def setUp(self):        # 设置全局引用
        self.driver.get("https://www.baidu.com/")
        sleep(3)
    def test_001(self):
        '''倒霉title'''
        t = self.driver.title    #实际结果
        print(t)            #打印结果
        ex = "百度一下，你就知道"    #期望结果
        self.assertEqual(t, ex)     #equal是相等的，平等的意思
    def test_002(self):
        '''输入孙悟空'''
        self.driver.find_element_by_css_selector("#kw").send_keys("孙悟空")
        print(s)

        sleep(2)
        p = self.driver.title
        print(p)
        eo = "孙悟空_百度搜索"
        self.assertEqual(p, eo)
    def test_003(self):
        '''测试截图'''
        ti = self.driver.title
        print(ti)
        self.assertEqual(ti, "百度一下，a")
    def tearDown(self):
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()