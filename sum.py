import sublime, sublime_plugin

class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')
        sum_view.insert(edit, 0, '42')
        sum_view.set_read_only(True)
        sum_view.set_scratch(True)
