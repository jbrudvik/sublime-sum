import unittest

from utils import *


class SumTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_int(self):
        self.assertTrue(is_int("5"))
        self.assertFalse(is_int("h"))

    def test_to_number(self):
        self.assertEqual(number_from_string("73"), 73)
        self.assertEqual(number_from_string("9.5"), 9.5)


if __name__ == '__main__':
    unittest.main()
