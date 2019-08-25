import sublime, sublime_plugin
import re

# Expand <letters,command,digits>/ into \frac{<stuff>}{}
# Uses regular expression to determine which to include in the numerator
# Implementation of Gilles Castel's code in ST


class FractionCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		point = view.sel()[0].b
		line = view.substr(sublime.Region(view.line(point).a, point))
		line = line[::-1]
		rex = re.compile(r"/(((\}\d+\{|\d)(\^|_))*([A-Za-z]+)(\\)?(\d*)|(\d+))")
		rex2 = re.compile(r"/(\s*)")
		expr = re.match(rex, line) # have numerator and /
		expr2 = re.match(rex2, line) # no numerator, but have /
		if expr:
			numerator = expr.group(1)[::-1]
			numerator_region = sublime.Region(point-len(numerator)-1,point)
			view.erase(edit, numerator_region)
			snippet = "\\\\frac{" + numerator + "}{$1}$0"
			view.run_command("insert_snippet", {'contents' : snippet})
			sublime.status_message("Fraction expanded")
		elif expr2:
			view.erase(edit, sublime.Region(point-1,point))
			snippet = "\\\\frac{$1}{$2}$0"
			view.run_command("insert_snippet", {'contents' : snippet})
			sublime.status_message("WARNING: no numerator detected")
		else:
			sublime.status_message("ERROR: could not find fractions to expand")
