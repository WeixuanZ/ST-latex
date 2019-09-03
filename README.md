# Snippets for LaTeX

Use in conjunction with [_LatexTools_](https://github.com/SublimeText/LaTeXTools), _LaTeX-cwl_ and _LaTeX Snippets_.

Some snippets are inspired by [gillescastel/latex-snippets](https://github.com/gillescastel/latex-snippets).

Use <kbd>Tab</kbd> to trigger.


# Plugin

**ST plugin for speeding up the input of LaTeX Maths**

The plugin [mathhelper.py](https://github.com/WeixuanZ/ST-LaTeX/blob/master/mathhelper.py) should be placed directly under `Packages/User/` and add the following to key-map settings.
```JSON
  {
    "keys": [
      "super+r"
    ],
    "command": "show_overlay",
    "args": {
      "overlay": "goto",
      "text": "@"
    }
  },
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
      "enter"
    ],
    "command": "chain",
    "args": {
      "commands": [
        [
          "intertext"
        ],
        [
          "reindent"
        ]
      ]
    },
    "context": [
      {
        "key": "selector",
        "operator": "equal",
        "operand": "text.tex.latex meta.environment.math.block.be.latex"
      }
    ]
  }
```

* Automatically surround superscripts or subscripts with more that two digits with `{` `}`

* Add `\left` and `\right` in front of a pair of matching brackets using <kbd>⌘</kbd>+<kbd>l</kbd>,<kbd>b</kbd>

* Fraction expansion is triggered by double hitting <kbd>/</kbd> in math environments, the railroad diagram of the regular expression behind it is shown below
`(((((\})([A-Za-z]|\d)+(\{)|(\d|[A-Za-z]))(\^|_))|(\)([A-Za-z]|\d)+\()|(}([A-Za-z]|\d)+{))*([A-Za-z]+)(\\)?([A-Za-z]?)(\d*)|(\d+))(\-?)`
  ![](image.png)
  
* Automatically wrap lines begin with two or more letters with `\intertext{}` command in _align_ environments
  For autoindent to work as expected, need the [_ChainOfCommand_](https://github.com/jisaacks/ChainOfCommand) plugin and add "reindent" macro after calling "intertext"
