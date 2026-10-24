## 🎃 Match-case vs If-else statements.

In **Python 3.10 and newer**, both **if-else chains** and **match-case statements** handle conditional flow. However, they serve fundamentally different purposes: **if-else** is designed for **boolean evaluation**, while **match-case** is built for **structural pattern matching** (if no case matches, none of the branches is executed).

> The underlying distinction is that `if` checks Boolean conditions, while `match` checks patterns

| Your decision involves… | Usually a clear choice |
| --- | --- |
| A few simple equality checks | Either |
| Several specific menu options | `match` |
| Numerical ranges or combinations of conditions | `if/elif/else` |
| Recognizing and unpacking lists, dictionaries, or objects | `match` |

**📚 References**

- [https://www.geeksforgeeks.org/python/python-match-case-statement/](https://www.geeksforgeeks.org/python/python-match-case-statement/)
- [https://docs.python.org/3/tutorial/controlflow.html#match-statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [https://www.w3schools.com/python/python_match.asp](https://www.w3schools.com/python/python_match.asp)

## 🎃 `continue` and `break` keywords

> The `continue` keyword in Python skips the remaining code inside the current loop iteration and immediately jumps to the next iteration. Unlike the `break` keyword, which stops the loop entirely, `continue` simply forces the loop to start its next cycle. In nested loops, both affect only the innermost enclosing loop.

## 🎃 Function docstrings

> A docstring should explain **how to use a function and what behavior to expect**, without requiring the reader to inspect its code. Document relevant side effects, such as modifying an argument. Keep implementation details in code comments unless they affect how the function is used.

For **Google-style docstrings**, include these sections when needed: 
- **`Args:`**: Describe the function’s parameters. 
- **`Returns:`**: Describe the returned value. 
- **`Raises:`**: Describe exceptions relevant to the caller.

Use consistent indentation of two or four spaces for section contents. A **one-line docstring** is enough when the function’s name, signature, and brief description clearly explain its behavior.

**📚 References**

- [Sphinx — Docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format)
- [Google Python Style Guide — Comments and docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [numpydoc — Docstring standard](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)