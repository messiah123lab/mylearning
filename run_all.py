import unittest
import os
import sys
import HTMLTestRunner_cn
import time
from tomorrow import threads
import random
from BeautifulReport import BeautifulReport


casepath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'testcase')

reportpath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'casereport')

discover=unittest.defaultTestLoader.discover(start_dir=casepath,pattern='test*.py',top_level_dir=None)

'''
批量执行用例，生成一份总的报告
'''
# time=time.strftime('%Y%m%d.%H.%M.%S')
# #
# fp=open(reportpath+'/%s.html'%time,'wb')
# runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
#                                         title='再看你一眼',
#                                         description='在某个平行的宇宙',
#                                         retry=1)
#
# runner.run(discover)


'''
启动3个线程执行用例，每个用例生成一份报告
'''
# @threads(3)
# def run(testmethod):
#     if testmethod:
#         timer = time.strftime('%Y%m%d.%H.%M.%S')
#         fp = open(reportpath + '/%d.html' % random.randint(1,100), 'wb')
#         runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
#                                                       title='%s' % timer,
#                                                       description='在某个平行的宇宙',
#                                                           retry=1)
#         runner.run(testmethod)
#         fp.close()


'''
启动3个线程执行用例，生成一份总的报告
'''
@threads(3)
def run(testmethod):
    if testmethod:
        result=BeautifulReport(testmethod)
        result.report(filename='report.html' ,
                      description='test' ,
                      log_path=reportpath)


if __name__=="__main__":
    for i in discover:
        run(i)