# -*- coding: utf-8 -*-
import unittest
import time
from common import HTMLTestReport
test_dir = "E:\JetBrains\PyCharm 5.0.4\jiejie\case"
dis = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                          pattern="test*.py",
                                          top_level_dir=None)
print(dis)
if __name__ == "__main__":
    now = time.strftime("%Y_%m_%d")
    filename = "E:\\JetBrains\\PyCharm 5.0.4\\jiejie\\report" + now +\
        "resut.html"
    fp = open(filename, "wb")
    runner = HTMLTestReport.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况：",
                                           verbosity=2, retry=1)
    runner.run(dis)