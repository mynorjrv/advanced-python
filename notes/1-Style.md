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

