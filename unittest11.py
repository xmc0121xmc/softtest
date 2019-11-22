import requests
import unittest
class Testadd(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("stop")

    def test_01(self):
        a = 1
        b = 1
        self.assertEqual(2, a+b)

    def test_02(self):
        a = 1
        b = 1
        self.assertEqual(3, a+b)

if __name__ == '__main__':
    unittest.main()
    print("this is v1")