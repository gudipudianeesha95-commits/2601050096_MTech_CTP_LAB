**EXPERIMENT 5 — Banking Management System**

The workbook specifies a Banking Management System demonstrating inheritance and abstraction with type hints.

**Aim**

To implement a Banking Management System using inheritance and abstraction.

**Algorithm**

1. Create an abstract Bank Account class.

2. Create Savings Account.

3. Implement deposit and display operations.

4. Create an account object.

5. Display the balance.

**Python Program**

from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod

    def display(self):
    
        pass


class SavingsAccount(Account):

    def __init__(self, name, balance):

        self.name = name
        
        self.balance = balance

    def display(self):
        
        print("Name:", self.name)
        
        print("Balance:", self.balance)


account = SavingsAccount("Aneesha", 5000)

account.display()

**Output**

Name: Aneesha


Balance: 5000

Data & Result

Account Holder = Aneesha

Balance = 5000

**Inference & Analysis**

Inheritance allows a child class to use the features of a parent class. Abstraction hides unnecessary implementation details.

**Result**

Thus, a simple Banking Management System was successfully implemented.
