import sublime, sublime_plugin
import re



###############################################################################

# ST plugin for speeding up the input of LaTeX maths

# Weixuan Zhang 1/9/2019

###############################################################################




# Automatically surround superscripts or subscripts with more that two digits with { }
# Map space key to this command

class SscriptCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		point = view.sel()[0].b
		line = view.substr(sublime.Region(view.line(point).a, point))
		
		rex = re.compile(r".*[A-Za-z](_|\^)(\d{2,})$")  # if there are two or more digits after _ or ^
		expr = re.match(rex, line)
		
		if expr:
			sscript = expr.group(2)  # the digits in subscript or superscript

			sscript_region = sublime.Region(point-len(sscript),point)
			view.erase(edit, sscript_region)
			snippet = "{" + sscript + "} $0"
			sublime.status_message("Subscript or superscript formatted")
			
		else:
			snippet = " "
		
		view.run_command("insert_snippet", {'contents' : snippet})





# Automatically add \left and \right in front of a pair of matching brackets
# Map super+l,b keys to this command

class LrbracketsCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		point = view.sel()[0].b
		line = view.substr(sublime.Region(view.line(point).a, point))

		rex = re.compile(r"(.+)\)$")  # matches anything with a ")" in front of the cursor
		expr = re.match(rex, line)

		if expr:  # if there is a right bracket in front of the cursor
			depth = 0  # depth of brackets
			i = len(line) -1  # index, minus 1 to start at 0

			while True:
				# adjusting the depth based on the nesting of brackets
				if line[i] == ')': depth += 1
				if line[i] == '(': depth -= 1

				# print("{}: index{} depth{}".format(line[i],i,depth))  # debugging

				if depth == 0:  # matching bracket found
					view.insert(edit,point-1,"\\right")
					view.insert(edit,view.line(point).a+i,"\\left")
					sublime.status_message("Left and right brackets formatted")
					break
				i -= 1  # if not found, search one character in front
				if i == -1:  # index out of range, no matching bracket found
					sublime.status_message("ERROR: no matching brackets")
					break

		else:  # there is no right bracket to start with
			sublime.status_message("ERROR: no right bracket")





# Expand <letters,command,digits>/ into \frac{<stuff>}{}
# Uses regular expression to determine which to include in the numerator
# Inspired by Gilles Castel's code for vim 
# Map /,/ keys to this command 

class FractionCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		point = view.sel()[0].b
		line = view.substr(sublime.Region(view.line(point).a, point))
		line = line[::-1]
		
		rex = re.compile(r"(((((\})([A-Za-z]|\d)+(\{)|(\d|[A-Za-z]))(\^|_))|(\)([A-Za-z]|\d)+\()|(}([A-Za-z]|\d)+{))*([A-Za-z]+)(\\)?([A-Za-z]?)(\d*)|(\d+))(\-?)")
		expr = re.match(rex, line)
		
		if expr:  # have numerator
			numerator = expr.group(1)[::-1]  # without the negative sign
			
			if expr.group(19):  # negative sign in front
				numerator_region = sublime.Region(point-len(numerator)-1,point)
				view.erase(edit, numerator_region)
				snippet = "-\\\\frac{" + numerator + "}{$1}$0"
			
			else:  # no negative sign
				numerator_region = sublime.Region(point-len(numerator),point)
				view.erase(edit, numerator_region)
				snippet = "\\\\frac{" + numerator + "}{$1}$0"
			view.run_command("insert_snippet", {'contents' : snippet})
			sublime.status_message("Fraction expanded")

		else:
			snippet = "\\\\frac{$1}{$2}$0"  # add an empty \frac{}{}
			view.run_command("insert_snippet", {'contents' : snippet})
			sublime.status_message("WARNING: no numerator detected")




# Automatically wrap lines begin with two or more letters with \intertext{} command in align environments
# Map enter to this command, and use ChainOfCommands plugin to add reindent command afterwards

class IntertextCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		view = self.view
		point = view.sel()[0].b
		line = view.substr(sublime.Region(view.line(point).a, point))

		rex = re.compile(r"^\s*([A-Za-z]{2,}.*)")
		expr = re.match(rex, line)

		if expr:
			text = expr.group(1)
			view.insert(edit,point-len(text),"\\intertext{")
			view.insert(edit,point+11,"}\n")
		else:
			view.insert(edit,point,"\\\\\n")  # normal behaviour of enter key







