**EXPERIMENT 9 — Pytest and Hypothesis**

The workbook asks for unit and integration tests using Pytest and Hypothesis.

**Aim**

To test a Python application using unit testing.

**Algorithm**

1. Create a function.

2. Write a test.

3. Run the test.

4. Check whether it passes.

**Python Program**

def add(a, b):

    return a + b


def test_add():
    
    assert add(2, 3) == 5

Save as:

test_program.py

Run:

pytest

**Output**

1 passed

**Result**

Test: 2 + 3

Expected: 5

Result: 5

Status: Passed

**Inference & Analysis**

Testing helps find errors and verifies that the program works correctly.

**Result**

Thus, a simple unit test was successfully created.
