# Best practices and Standardization

## PEPs

Stands for **Python Enhancement Proposals**, they are a collection of online documents that outlines the language standards and provides information about many changes and processes related to Python.

There are a lot of PEPs, the index can be found in the [https://peps.python.org/](PEP 0). For now we are focusing on four:

- PEP 1 - PEP Purpose and Guidelines, which provides information about the purpose of PEPs, their types, and introduces general guidelines;
- PEP 8 – Style Guide for Python Code, which gives conventions and presents best practices for Python coding;
- PEP 20 – The Zen of Python, which presents a list of principles for Python’s design;
- PEP 257 – Docstring Conventions, which provides guidelines for conventions and semantics associated with Python docstrings.

## PEP 1: PEP Purpose and Guidelines

From the PEP itself: 

> PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

According to Edube, a PEP is a collection of guidelines, best practices, descriptions of (new) features and implementations, as well as processes, mechanisms and important information surrounding Python.

### Types of PEPs

There are three kinds of PEPs:


- **Standards Track** PEPs, which describe new language features and implementations;
- **Informational** PEPs, which describe Python design issues, as well as provide guidelines and information to the Python community;
- **Process** PEPs, which describe various processes that revolve around Python (e.g., propose changes, provide recommendations, specify certain procedures). Process PEPs are like Standards Track PEPs but apply to areas other than the Python language itself.

### PEP Audience

Literally from the PEP itself:

> The typical primary audience for PEPs are the core developers of the CPython reference interpreter and their elected Steering Council, as well as developers of other implementations of the Python language specification.

> However, other parts of the Python community may also choose to use the process (particularly for Informational PEPs) to document expected API conventions and to manage complex design coordination problems that require collaboration across multiple projects.

### PEP workflow

Again... All taken from the PEP itsel:

The PEP process begins with a new idea for Python. It is highly recommended that a single PEP contain a single key proposal or new idea; the more focused the PEP, the more successful it tends to be.

Each PEP must have a champion (a.k.a. Author) – someone who writes the PEP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea.

Formats, templates and the submission process as well as subsequent stages are all described in PEP 1.

Also, the PEP defines:


- Python’s Steering Council, i.e., a five-person committee and the final authorities who accept or reject PEPs;
- Python’s Core Developers, i.e., the group of volunteers who manage Python, and;
- Python’s BDFL, i.e., Guido van Rossum, the original creator of Python, who served as the project’s Benevolent Dictator For Life until 2018, when he resigned from the decision-making process. This title changed, and PEP-Delegate is used instead of BDFL-Delegate.


## PEP 20: The Zen of Python

The Zen of Python is a collection of 19 aphorisms, which reflect the philosophy behind Python, its guiding principles, and design.

Tim Peters, a long time major contributor to the Python programming language and Python community, wrote this 19-line "poem" on the Python mailing list in 1999, and it became entry #20 in the Python Enhancement Proposals in 2004.

This aphorisms are included in the interpreter, they can be seen when running `import this`.

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Some specific highlights:

- `import *` is just recommended in interacive environments
- OOP is useful in data oriented solutions, funcional is better in procedures
- Usually three identation levels is enough
- But nesting should be balanced with density
- Code is read more often thatn it is written, give meaningful names
- Sticking to conventions already implemented to ensure backward compatibility could be the only special case
- It is better to fail fast
- Testing saves time
- Names must not be ambiguous
- Remember single responsability principle
- Dont rush but good enough is good enough
- What can be explained with words can be translated to code
- And `module.function` apparently is better than `from module import function`

## PEP 8: Style Guide for Python Code

This pep gives coding conventions for the Python code in the standard library, but it is useful for any Python programmer.

### A foolish consistency is the Hobgoblin of little minds

The style guide is intended to improve readability, and is about consistency. Consistency within one module or function is the most important and then goes within a project and then with the style guide.

Sometimes style guide recommendations just aren’t applicable. When in doubt, use your best judgment.

In particular: do not break backwards compatibility just to comply with this PEP!

Some other good reasons to ignore a particular guideline:

1. When applying the guideline would make the code less readable, even for someone who is used to reading code that follows this PEP.
2. To be consistent with surrounding code that also breaks it (maybe for historic reasons) – although this is also an opportunity to clean up someone else’s mess (in true XP style).
3. Because the code in question predates the introduction of the guideline and there is no other reason to be modifying that code.
4. When the code needs to remain compatible with older versions of Python that don’t support the feature recommended by the style guide.

### Code layout

Indentation:

- 4 spaces per level
- spaces, not tabs :)
- Functions arguments should be indented
- if statements are funny xd
- Closing brace/brackets/parenthesis may or may not be indented

Line length:

- Max 79 characters
- Docstrings or commets 72 charactes, strictly
- The preferred way of wrapping is implicit line continuation inside braces
- Backslashes may be used in older versions than 3.10 in with or assert statements

Binary operators:

- line breaks comes before binary operations

Blank lines: 

- Top-level functions and class surrounded by two lines
- methods inside classes surrounded by a single blank line
- Extra blank lines may be used to separate groups of functions
- Blank lines should indicate logical sections

File encoding:

- Code in the core Python distribution should always use UTF-8, and should not have an encoding declaration
- non-ASCII characters may be used for places and humans, avoid noisy ones
- All identifiers must use ASCII-only characters
- Identifiers should use English

Imports:

- Imports should be on separate lines
- `from x import a, b` its okay
- Standard library, then Third party, then Local specific imports
- Absolute imports are recommended
- Relative imports (`from . import sibling` or `from .sibling import example`) are acceptable in complex package layouts, but they should be avoided
- It is okay to import class names `from myclass import MyClass`, if this causes local name clashes import the module and spell the class explicitly `myclass.MyClass`

Module dunders:

- After module docstring
- before imports except `from __future__`

### String quotes

No preference xd except for triple-quoted strings where double quotes are used.

### Whitespace

Agh xd so much rules

Buuuuut, a curious one. `:` in slicing is treated as a binary operation so it is suggested the same space before and after. For example `a[1:10:3]` and `a[1 : 10 : 3]`. Also, `:` in dicts are usually `a={1: 'hello'}.

### Naming conventions

Overriding principle: Names visible to the user should reflect usage rather than implementation.

Naming styles:

- `b` (single lowercase letter)
- `B` (single uppercase letter)
- `lowercase`
- `lowercase_with_underscores`
- `UPPERCASE`
- `UPPERCASE_WITH_UNDERSCORES`
- `CamelCase` (or `CapWords`) (should capitalize all letters of acronyms)
- `mixedCase`

Special styles:

- `_single_leading_underscore`: weak internal use, `from M import *` does not import these.
- `single_trailing_underscore_`: used to avoid collisions with Python keywords.
- `__double_leading_underscore`: when naming class attributes, invokes name mangling.
- `__double_leading_and_trailing_underscore__`: reserved for magic objects.

Naming conventions:

- Avoid 'l', 'O' and 'I'
- Identifiers must be ASCII compatible
- Packages and modules names should have short, lowercase names. Underscores may be used in modules for readability, but not in packages.
- Class names should use `CapWords`. If it is mainly used as a callable, convention for functions may be used.
- Type variables name should be short and use `CapWords`. `_co` and `_contra` suffixes are used for covariant or contravariant behavior.
- Exceptions names follows class names, they may add the `Error` suffix.
- Function and variable names should be lowercase, with words separated by underscores.
- `self` for instance methods, `cls` for class methods, and the use of trailing underscore if a reserved keyword is going to be used (a synonym is suggested).
- Constants should be in uppercase


## PEP 257: Docstring Conventions

