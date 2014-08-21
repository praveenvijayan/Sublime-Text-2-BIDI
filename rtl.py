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
		bidiRegion(region, self.view, edit)

class bidiselectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selectionSet = self.view.sel()
		for selectionRegion in selectionSet:
			bidiRegion(selectionRegion, self.view, edit)

def bidiRegion(region, view, edit):
	txt = view.substr(region)
	reshaped_text = reshape(txt)
	bdiText = get_display(reshaped_text)
	view.replace(edit, region, bdiText)