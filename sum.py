import sublime
import sublime_plugin
import re

from utils import *


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
