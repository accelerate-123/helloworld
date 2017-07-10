#!/usr/loca/bin/python3
# -*- coding:utf-8 -*-

from HTMLTestRunner import HTMLTestRunner
import time,sys
import unittest

sys.path.append('./case')

test_dir='./case'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
	now=time.strftime("%Y-%m-%d %H_%M_%S")
	filename='./report/'+now+'_result.html'

	fp=open(filename,'wb')
	runner=HTMLTestRunner(stream=fp,
			title='test report',
			description='report')
	runner.run(discover)
	fp.close()
