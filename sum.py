import sublime, sublime_plugin

class SumCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.insert(edit, 0, '42')