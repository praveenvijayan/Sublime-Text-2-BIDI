import sublime, sublime_plugin, sys
sys.path.append( 'lang' )
from algorithm import get_display

class bidiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		txt = self.view.substr(region)
		bdiText = get_display(txt, upper_is_rtl=True)
		self.view.replace(edit, region, bdiText)