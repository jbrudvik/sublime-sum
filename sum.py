import sublime
import sublime_plugin

from utils import *


class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Create new buffer
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')

        # Insert sum of numbers from original buffer into new buffer
        file_text = self.view.substr(sublime.Region(0, self.view.size()))
        file_sum = sum_of_numbers_in_string(file_text)
        sum_view.insert(edit, 0, str(file_sum))

        # Make new buffer read-only and never report dirty status
        sum_view.set_read_only(True)
        sum_view.set_scratch(True)
