# Snippets for LaTeX

Use in conjunction with [_LatexTools_](https://github.com/SublimeText/LaTeXTools), _LaTeX-cwl_ and _LaTeX Snippets_.

Some snippets are inspired by [gillescastel/latex-snippets](https://github.com/gillescastel/latex-snippets).

Use <kbd>Tab</kbd> to trigger.


# Plugin

**ST plugin for speeding up the input of LaTeX Maths**

The plugin [mathhelper.py](https://github.com/WeixuanZ/ST-snippets/blob/master/LaTeX/mathhelper.py) should be placed directly under `Packages/User/` and add the following to key-map settings.
```JSON
  {
    "keys": [
      "/",
      "/"
    ],
    "args": {
      "file": "Packages/User/mathhelper.py"
    },
    "context": [
      {
        "key": "selector",
        "operator": "equal",
        "operand": "text.tex.latex meta.environment.math"
      }
    ],
    "command": "fraction"
  },
  {
    "keys": [
      " "
    ],
    "args": {
      "file": "Packages/User/mathhelper.py"
    },
    "context": [
      {
        "key": "selector",
        "operator": "equal",
        "operand": "text.tex.latex meta.environment.math"
      }
    ],
    "command": "sscript"
  },
    {
    "keys": [
      "super+l",
      "b"
    ],
    "args": {
      "file": "Packages/User/mathhelper.py"
    },
    "context": [
      {
        "key": "selector",
        "operator": "equal",
        "operand": "text.tex.latex meta.environment.math"
      }
    ],
    "command": "lrbrackets"
  }
```

* Automatically surround superscripts or subscripts with more that two digits with { }

* Add `\left` and `\right` in front of a pair of matching brackets using <kbd>⌘+l,b</kbd>

* Fraction expansion is triggered by double hitting <kbd>/</kbd> in math environments, the railroad diagram of the regular expression behind it is shown below
  ![](image.png)
