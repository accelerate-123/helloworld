#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import unittest
from test011 import Calculator

class CountTest(unittest.TestCase):
    def setUp(self):
        self.cal=Calculator(8,4)

    def tearDown(self):
        pass

    def test_add(self):
        result=self.cal.add()
        self.assertEqual(result,12)

    def test_sub(self):
        result=self.cal.sub()
        self.assertEqual(result,4)

    def test_mul(self):
        result=self.cal.mul()
        self.assertEqual(result,32)

    def test_div(self):
        result=self.cal.div()
        self.assertEqual(result,2)

if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(CountTest("test_add"))
    suite.addTest(CountTest("test_sub"))

    runner=unittest.TextTestRunner()
    runner.run(suite)