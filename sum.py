import sublime, sublime_plugin

class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')

        file_text = self.view.substr(sublime.Region(0, self.view.size()))
        sum_view.insert(edit, 0, file_text)

        sum_view.set_read_only(True)
        sum_view.set_scratch(True)
