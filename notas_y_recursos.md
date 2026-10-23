## 🐍 Python Match-case Statement:

- https://www.geeksforgeeks.org/python/python-match-case-statement/
- https://docs.python.org/3/tutorial/controlflow.html#match-statements
- https://www.w3schools.com/python/python_match.asp

---

### ☕ Match-case vs If-else statements.

In **Python 3.10 and newer**, both **if-else chains** and **match-case statements** handle conditional flow.

However, they serve fundamentally different purposes: **if-else** is designed for **boolean evaluation**, while **match-case** is built for **structural pattern matching**.

> The underlying distinction is that `if` checks Boolean conditions, while `match` checks patterns

| Your decision involves… | Usually a clear choice |
| --- | --- |
| A few simple equality checks | Either |
| Several specific menu options | `match` |
| Numerical ranges or combinations of conditions | `if/elif/else` |
| Recognizing and unpacking lists, dictionaries, or objects | `match` |