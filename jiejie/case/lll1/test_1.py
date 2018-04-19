# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep

class Ceshi(unittest.TestCase):
    '''百度查询用例'''
    @classmethod    # 类方法
    def setUpClass(cls):
        '''进入百度的用例'''
        cls.driver = webdriver.Firefox()
        print("只打开一次浏览器")
        print("只登陆一次")

    def setUp(self):
        self.driver.get("https://www.baidu.com/")
        sleep(3)
    def tearDown(self):
        self.driver.delete_all_cookies()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("最后关掉")

    def test_003(self):
        '''对比百度title'''
        t = self.driver.title    #实际结果
        print(t)            #打印结果
        ex = "百度一下，你就知道"    #期望结果
        self.assertEqual(t, ex)     #equal是相等的，平等的意思
    def test_004(self):
        '''输入刘东杰进行查询'''
        self.driver.find_element_by_css_selector("#kw").send_keys("刘东杰")
        sleep(2)
        p = self.driver.title
        print(p)
        eo = "刘东杰_百度搜索1"
        self.assertEqual(p, eo)
        sleep(3)
    def test_005(self):
        '''输入白素萍进行查询'''
        self.driver.find_element_by_css_selector("#kw").send_keys("白素萍")
        sleep(2)
        p1 = self.driver.title
        print(p1)
        #输入白素萍进行查询
        eo1 = "白素萍_百度搜索"
        self.assertEqual(p1, eo1)
        sleep(2)
