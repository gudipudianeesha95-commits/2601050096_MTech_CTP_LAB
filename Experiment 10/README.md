**EXPERIMENT 10 — mypy, Docker and GitHub Actions**

The workbook asks to configure mypy, Docker and GitHub Actions CI/CD for an existing Python project.

**Aim**

To configure type checking, Docker and CI/CD for a Python project.

**Algorithm**

Create a Python program.

Add type hints.

Run mypy.

Create a Dockerfile.

Configure GitHub Actions.

Run the project automatically.

**Python Program**

def add(a: int, b: int) -> int:
    
    return a + b


result = add(10, 20)

print("Result:", result)

**Output**

Result: 30

**Data & Result**

Input: 10, 20

Output: 30

Type checking: Successful

**Inference & Analysis**

Type hints help identify incorrect data types. Docker provides a consistent environment, while GitHub Actions can automate testing.

**Result**

Thus, the Python project was prepared for type checking and automated development workflows.
