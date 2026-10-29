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

## 🎃 Designing Functions

A function’s **domain**, **range**, and **behavior** describe conceptual aspects of what it is meant to do.

- **Domain:** the set of all inputs a function might take as arguments.
- **Range:** the set of output values a function might return.
- **Behavior of a pure function:** the relationship it creates between input and output.

**Examples**

| Function | Domain: possible inputs | Range: possible outputs | Behavior: relationship between input and output | Example call and output |
| --- | --- | --- | --- | --- |
| `square(x)` | Real numbers: $x \in \mathbb{R}$. | Nonnegative real numbers: $y \geq 0$. | Returns the square of the input: $y = x^2$. | `square(-3)` → `9` |
| `fib(n)` | Integers greater than or equal to one: $n \in \mathbb{Z},\ n \geq 1$. | Fibonacci numbers, using $F_1 = 1$ and $F_2 = 1$: $1, 2, 3, 5, 8, \ldots$. | Returns the Fibonacci number at the position specified by the input: $y = F_n$. | `fib(6)` → `8` |

**A Guide to Designing Functions**

Good function design reinforces the idea that **functions are abstractions**.

- **Each function should have one clear job.** Its job should be identifiable with a short name and explainable in one sentence. Divide functions that perform several distinct jobs into smaller functions.

- **Don’t Repeat Yourself (DRY).** Define repeated logic once, give it a name, and reuse it. Copying and pasting code may reveal an opportunity for **functional abstraction**.

- **Define functions generally.** Use a general operation when it covers several related cases. For example, squaring is a special case of `pow(base, exponent)`, which raises a base to a specified power.

These guidelines improve readability, reduce opportunities for errors, and often reduce the amount of code written. Decomposing complex tasks into concise functions takes practice.

**📚 Reference**

DeNero, J. (n.d.). *1.4 Designing functions*. Composing Programs. [https://composingprograms.com/3ed/designing-functions/](https://composingprograms.com/3ed/designing-functions/)
