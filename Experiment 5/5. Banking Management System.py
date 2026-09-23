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