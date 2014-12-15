# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import re


class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')

        file_text = self.view.substr(sublime.Region(0, self.view.size()))
        words = [s for s in re.split('[\s,[\](){}]', file_text)]
        stripped_words = [strip_currency(s) for s in words]
        numbers = [to_number(s) for s in stripped_words if is_number(s)]
        result = sum(numbers)

        sum_view.insert(edit, 0, str(result))
        sum_view.set_read_only(True)
        sum_view.set_scratch(True)


def strip_currency(s):
    """
    Return a string without leading or trailing currency symbols

    Strip leading and trailing currency symbols, and currency symbols
    at position 1 if first character is + or -
    """
    currency_symbols = '$€£¥¢'
    s = s.strip(currency_symbols)
    if len(s) > 2 and s[0] in '+-' and s[1] in currency_symbols:
        s = s[0] + s[2:]
    return s


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


def to_number(s):
    """
    Parse and return number from string.

    Return float only if number is not an int. Assume number can be parsed from
    string.
    """
    try:
        return int(s)
    except ValueError:
        return float(s)
