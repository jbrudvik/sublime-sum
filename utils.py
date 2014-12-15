# -*- coding: utf-8 -*-

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
