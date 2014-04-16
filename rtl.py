import sublime, sublime_plugin, sys

sys.path.append( 'bidi' )
try:

    # Python 3

    from .bidi.arabic_reshaper import reshape
    from .bidi.algorithm import get_display
except ValueError:

    # Python 2

    from bidi.arabic_reshaper import reshape
    from bidi.algorithm import get_display

class bidiCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0, self.view.size())
		txt = self.view.substr(region)
		reshaped_text = reshape(txt)
		bdiText = get_display(reshaped_text)
		self.view.replace(edit, region, bdiText)
