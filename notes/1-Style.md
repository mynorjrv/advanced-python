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

Again, taking directly from the pep itself.

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the `__doc__` special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the __init__ constructor) should also have docstrings. A package may be documented in the module docstring of the __init__.py file in the package directory.

There are two other types of docstrings, they are not recognized by the bytecode compiler but may be extracted by software tools:

1. String literals occurring immediately after a simple assignment at the top level of a module, class, or `__init__` method are called “attribute docstrings”.
2. String literals occurring immediately after another docstring are called “additional docstrings”.

For consistency, always use `"""triple double quotes"""` around docstrings. Use `r"""raw triple double quotes"""` if you use any backslashes in your docstrings.

### One-line Docstring

One-liners are for really obvious cases. They should really fit on one line.

```Python
def kos_root():
    """Return the pathname of the KOS root directory."""
    global _kos_root # Please ignore the bad practices xd
    if _kos_root: return _kos_root
    ...
```

The docstring is a phrase ending in a period. It prescribes the function or method’s effect as a command (“Do this”, “Return that”), not as a description; e.g. don’t write “Returns the pathname …”.

The one-line docstring should NOT be a “signature” reiterating the function/method parameters (which can be obtained by introspection). This type of docstring is only appropriate for C functions (such as built-ins), where introspection is not possible. However, the nature of the return value cannot be determined by introspection, so it should be mentioned.

### Multi-line Docstrings

Its a lot xd

Letsssss just give an example xd

```Python
def complex_num(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```

### Accessing docstrings

Simple, so just an example:

```Python
def my_fun(a, b):
    """The summary line goes here.

    A more elaborate description of the function.

    Parameters:
    a: int (description)
    b: int (description)

    Returns:
    int: Description of the return value.
    """
    return a*b

print(my_fun.__doc__)
```

## PEP 484: Type Hints

This PEP introduce the `typing` module which was a provisional solution.

from edube, it's an optional, but more formalized, feature that makes it possible for you to use the Python built-in `typing` module to provide type hint information in your code in order to leave certain suggestions, mark certain possible problems that may come up in the development process, and label specific names with type information.

An example:

```Python
# Type information added to a function:
def hello(name: str) -> str:
    return "Hello, " + name
```

Type hinting is optional, which means PEP 848 does not obligate you to leave any static typing-related information.

Why would you want type hinting?

- Type hinting can help you document your code. Instead of leaving argument- and response-related information in docstrings, you can use the language itself to serve this purpose. 
- Type hinting allows you to notice certain kinds of errors more effectively and write a more beautiful and, most of all, cleaner code.
- Type hinting does not have any effect on the operation of your code. It is ignored at runtime. This means there is no impact on performance.

Another related peps are: [https://peps.python.org/pep-0483/](PEP 483) and [https://peps.python.org/pep-3107/](PEP 3107).


## General tips for documenting a project

When documenting, depending on the nature of the project, you should first define its users and think about their needs. You can improve the user experience by thinking about how they are going to utilize your code and trying to predict common issues.

A project should contain the following documentation elements:

- a **readme**, which provides a brief summary of the project, its purpose, and possibly some installation guidelines;
- an **examples.py** file, which is a script that demonstrates a few examples of how to utilize the project (or a quickstart i guess);
- a **license** in the form of a txt file (particularly important for Open Source and Public Domain projects);
- a **how to contribute** file which provides information about the possible ways of contributing to the project (shared, open source, and public domain projects).

## Linters and fixers

Linters are tools that helps you write code. The linter analyzes your code for any stylistic anomalies and programming errors against a set of pre-defined rules.

Some examples are Flake8, Pylint, Pyflakes, Pychecker, Mypy, and Pycodestyle (formerly Pep8).

A fixer, on the other hand, is a program that helps you fix these issues and format your code to be consistent with the adopted standards. The most popular fixers are: Black, YAPF, and autopep8.