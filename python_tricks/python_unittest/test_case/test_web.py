# -*- coding:utf-8 -*-
# date:2018-03-14 16:27
# auther:yang

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class SearchWithBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.baidu.com")
        self.assertIn("百度一下，你就知道", driver.title)
        elem = driver.find_element_by_name("wd")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)
        sleep(3)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()