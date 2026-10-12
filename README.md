# is212-week11 – Refactoring

Three small exercises for the IS212 Week 11 lab. Each folder contains some smelly (but working!) code and a set of unit tests that currently all pass. A GitHub Actions workflow runs each exercise's tests whenever a file in that folder changes.

| Folder | Code smell | Refactoring | Who does it |
|---|---|---|---|
| `ex1` | Long Method | Extract Method | You (no AI) |
| `ex2` | Switch Statements | Replace Conditional with Polymorphism | Your AI assistant – you review |
| `ex3` | Duplicate Code | Your choice (e.g. Extract Superclass / Pull Up Method) | Your AI assistant, with a constrained prompt – you review |

## Getting started

1. Fork this repository (keep the name `is212-week11`).
2. Clone your fork and check that all the tests pass:

   ```
   python ex1/ex1_unit_tests.py
   python ex2/ex2_unit_tests.py
   python ex3/ex3_unit_tests.py
   ```

3. Follow the lab sheet on eLearn.

No packages need to be installed – the tests use Python's built-in `unittest`.
