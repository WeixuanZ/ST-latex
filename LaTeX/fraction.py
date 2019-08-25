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
		rex = re.compile(r"/(((\{\d+\}|\d)(\^|_))*(\d+)|([A-Za-z]+)(\\)?(\d*))")
		expr = re.match(rex, line)
		if expr:
			numerator = expr.group(1)[::-1]
			if numerator:
				numerator_region = sublime.Region(point-len(numerator)-1,point)
				view.erase(edit, numerator_region)
				snippet = "\\\\frac{" + numerator + "}{$1}$0"
			else:
				snippet = "\\\\frac{$1}{$2}$0"
			view.run_command("insert_snippet", {'contents' : snippet})
		else:
			sublime.status_message("ERROR: could not find fractions to expand")



