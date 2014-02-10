import sublime, sublime_plugin

class SumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sum_view = self.view.window().new_file()
        sum_view.set_name('Sum')

        file_text = self.view.substr(sublime.Region(0, self.view.size()))

        numbers = []
        for s in file_text.split():
            try:
                numbers.append(int(s))
            except ValueError:
                try:
                    numbers.append(float(s))
                except ValueError:
                    pass

        result = sum(numbers)
        sum_view.insert(edit, 0, str(result))

        sum_view.set_read_only(True)
        sum_view.set_scratch(True)
