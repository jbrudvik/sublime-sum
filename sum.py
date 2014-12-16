# -*- coding: utf-8 -*-

import re

try:
    import sublime
    import sublime_plugin

    class SumCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            # Create new buffer that never reports dirty status
            sum_view = self.view.window().new_file()
            sum_view.set_name('Sum')
            sum_view.set_scratch(True)

            # Insert sum of numbers from original buffer into new buffer
            file_text = self.view.substr(sublime.Region(0, self.view.size()))
            file_sum = sum_of_numbers_in_string(file_text)
            sum_view.insert(edit, 0, str(file_sum))

            # Make new buffer read-only
            sum_view.set_read_only(True)
except ImportError:
    pass


def is_int(s):
    """Return boolean indicating whether a string can be parsed to an int."""
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    """Return boolean indicating whether a string can be parsed to an float."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_number(s):
    """
    Return boolean indicating whether a string can be parsed to a number.

    Legal numbers are of int or float type.
    """
    return is_int(s) or is_float(s)


def number_from_string(s):
    """
    Parse and return number from string.

    Return float only if number is not an int. Assume number can be parsed from
    string.
    """
    try:
        return int(s)
    except ValueError:
        return float(s)


def words_in_string(s):
    """
    Return a list of words aggressively split from the string.

    Split on whitespace and some punctuation.
    """
    return re.split('[\s,[\](){}]', s)


def string_without_currency(s):
    """
    Return a string without leading or trailing currency symbols.

    Strip leading and trailing currency symbols, and currency symbols
    at position 1 if first character is + or -
    """
    currency_symbols = '$€£¥¢'
    s = s.strip(currency_symbols)
    if len(s) > 2 and s[0] in '+-' and s[1] in currency_symbols:
        s = s[0] + s[2:]
    return s


def sum_of_numbers_in_string(s):
    """
    Return sum of numbers in string.

    Make a best guess at what are summable numbers given unknown format.
    Strip some punctuation and currency symbols.
    """
    words = [string_without_currency(word) for word in words_in_string(s)]
    numbers = [number_from_string(word) for word in words if is_number(word)]
    return sum(numbers)
