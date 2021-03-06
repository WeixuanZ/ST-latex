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
      },
      { "key": "auto_complete_visible", 
        "operator": "equal", 
        "operand": false 
      }
    ]
  }
```

* Automatically surround superscripts or subscripts with more that two digits with `{` `}`

* Add `\left` and `\right` in front of a pair of matching brackets using <kbd>⌘</kbd>+<kbd>l</kbd>,<kbd>b</kbd>

* Fraction expansion is triggered by double hitting <kbd>/</kbd> in math environments, the railroad diagram of the regular expression behind it is shown below
`(((((\})([A-Za-z]|\d)+(\{)|(\d|[A-Za-z]))(\^|_))|(\)([A-Za-z]|\d)+\()|(}([A-Za-z]|\d)+{))*([A-Za-z]+)(\\)?([A-Za-z]?)(\d*)|(\d+))(\-?)`
  ![](image.png)
  
* Automatically wrap lines begin with two or more letters with `\intertext{}` command and add `\\` at the end of other lines containing an equal sign in _align_ environments
  For autoindent to work as expected, need the [_ChainOfCommand_](https://github.com/jisaacks/ChainOfCommand) plugin and add "reindent" macro after calling "intertext". Note that the `auto_complete_visible` key is used to ensure autocompletion can be selected when visible.


# Other Bits

## Python code highlighting
Add the following code into the `contexts` of the LaTeX syntax file to enable Python code highlighting inside _pythontex_ environments/commands
```YAML
  # pythontex package
  pythontex:
    - match: ((\\)begin)(\{)((pycode)|(pyblock)|(pyverbatim)|(pysub)|(sympycode)|(sympyblock)|(sympyverbatim)|(sympysub))(\})
      captures:
        1: support.function.begin.latex keyword.control.flow.begin.latex
        2: punctuation.definition.backslash.latex
        3: punctuation.definition.group.brace.begin.latex
        4: variable.parameter.function.latex
        13: punctuation.definition.group.brace.end.latex
      embed: scope:source.python
      embed_scope: meta.environment.embedded.python.latex source.python.embedded
      escape: '(?=\\end\{((pycode)|(pyblock)|(pyverbatim)|(pysub)|(sympycode)|(sympyblock)|(sympyverbatim)|(sympysub))\})'
    
    - match: (\\)((py)|(pyc)|(pyb)|(pyv)|(pys))\b
      captures:
        0: support.function.general.latex
        1: punctuation.definition.backslash.latex
      embed: scope:source.python
      embed_scope: meta.environment.embedded.python.latex source.python.embedded
      escape: '\}'
```

## Auto update using _latexmk_
Create a new builder with the following contents, and place the [.latexmkrc](https://github.com/WeixuanZ/ST-LaTeX/blob/master/.latexmkrc) in the working directory
```JSON
{
  "shell_cmd": "latexmk -cd -pvc -pdf -synctex=1 -interaction=nonstopmode $file",
  "selector": "text.tex.latex"
}
```

## Using other plugins

* _BracketHighlighter_ is customised so that `\left(` and `\right)` are highlighted
* Use _TodoReview_ to display TODOs in the form of `%TODO <text>`
* Use _Inc_dec_value_ to cycle through text-size commands (e.g. `tiny`, `normalsize`, `large`)
