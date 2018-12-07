# -*- coding: utf-8 -*-
import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class DummyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dummy(self):
        assert False == True


if __name__ == '__main__':
    unittest.main(verbosity=2)
