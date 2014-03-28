import sublime, sublime_plugin, sys
sys.path.append( 'lang' )
import bidi.arabic_reshaper
from bidi.algorithm import get_display

class bidiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		txt = self.view.substr(region)
		reshaped_text = bidi.arabic_reshaper.reshape(txt)
		bdiText = get_display(reshaped_text)
		self.view.replace(edit, region, bdiText)
