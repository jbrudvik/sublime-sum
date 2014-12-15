import unittest


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

    def test_one(self):
        self.assertEqual(True, True)

    def test_two(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
