import sublime, sublime_plugin
import re

class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')

        file_text = self.view.substr(sublime.Region(0, self.view.size()))
        words = [s for s in re.split('[\s,[\](){}]', file_text)]
        numbers = [to_number(s) for s in words if is_number(s)]
        result = sum(numbers)

        sum_view.insert(edit, 0, str(result))
        sum_view.set_read_only(True)
        sum_view.set_scratch(True)

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
    """Return boolean indicating whether a string can be parsed to an int or float."""
    return is_int(s) or is_float(s)

def to_number(s):
    """
    Parse and return number from string.

    Return float only if number is not an int. Assume number can be parsed from string.
    """
    try:
        return int(s)
    except ValueError:
        return float(s)
