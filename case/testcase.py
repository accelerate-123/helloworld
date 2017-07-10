#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner

class StringTestCase(unittest.TestCase):
    def setUp(self):
        self.test_string="This is a string"

    def tearDown(self):
        pass

    def test_Reverse(self):
        self.assertEqual("gnirts a si sihT",self.test_string[::-1])

    def test_Split(self):
        expected=['This','is','a','string']
        self.assertEqual(expected,self.test_string.split(' '))
        self.assertEqual(expected,self.test_string.split())

    def test_lower(self):
        self.assertEqual('this is a string',self.test_string.lower())

    def test_upper(self):
        self.assertEqual('THIS IS A STRING',self.test_string.upper())


if __name__=='__main__':
#    unittest.main()
    HTMLTestRunner.main()
