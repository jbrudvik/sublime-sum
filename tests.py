# -*- coding: utf-8 -*-

import unittest
from sum import *


class SumTestCase(unittest.TestCase):

    def test_is_float(self):
        floats = ("1.0", "-3", "-33.9", "5", 70, -9.2, 8)
        for f in floats:
            self.assertTrue(is_float(f))

        non_floats = ("p", "test")
        for n in non_floats:
            self.assertFalse(is_float(n))

    def test_number_from_string(self):
        known_values = (("73", 73),
                        ("9.5", 9.5))
        for s, number in known_values:
            self.assertEqual(number_from_string(s), number)

        non_number_strings = ("f", "hello", "-")
        for s in non_number_strings:
            self.assertRaises(ValueError, number_from_string, s)

    def test_words_in_string(self):
        known_values = (("there are 6 words in here",
                        ["there", "are", "6", "words", "in", "here"]),
                        ("(two words)",
                        ["two", "words"]))
        for s, words in known_values:
            self.assertEqual(words_in_string(s), words)

    def test_string_without_currency(self):
        known_values = (("$1", "1"),
                        ("1$", "1"),
                        ("+$1", "+1"),
                        ("-$1", "-1"),
                        ("$100", "100"),
                        ("1$00", "1$00"))
        for s, s_without in known_values:
            self.assertEqual(string_without_currency(s), s_without)

    def test_sum_of_numbers_in_string(self):
        known_values = (("1 2 3 4 5", 15),
                        ("1,2,3,4,5", 15),
                        ("1 2 3 4 5 6 7 8 9 10", 55),
                        ("1, 2, 3, 4, 5, 6, 7, 8, 9, 10", 55),
                        ("-5 -4 -3 -2 -1 0 1 2 3 4 5", 0),
                        ("", 0),
                        ("There are no numbers in this string", 0),
                        ("There is one number in this string: 7.5", 7.5),
                        ("1.0 3", 4.0),
                        ("{1.0,2,3,4,5,6,7,8,9,10}", 55.0),
                        ("[1,2,3,4,5,6,7,8,9,10]", 55),
                        ("(1,2,3,4,5,6,7,8,9,10)", 55),
                        ("+$97", 97),
                        ("$1500 -$1200", 300),
                        ("$101.50", 101.50),
                        ("101.53$", 101.53),
                        ("€5392", 5392),
                        ("928.99€", 928.99),
                        ("£5691929", 5691929),
                        ("3.14£", 3.14),
                        ("¥8.2", 8.2),
                        ("-8¥", -8),
                        ("¢84", 84),
                        ("38.42¢", 38.42),
                        ("""$328 in checking account.
                            About to transfer -$125 to savings.
                            Will pay -$159 now on credit card.""", 44),
                        ("""
                            1,000
                            2,000
                            3,000
                            """, 6))
        for s, sum_of_numbers in known_values:
            self.assertEqual(sum_of_numbers_in_string(s), sum_of_numbers)


if __name__ == '__main__':
    unittest.main()
