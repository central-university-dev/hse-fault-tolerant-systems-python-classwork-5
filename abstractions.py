from abc import ABC, abstractmethod


class BaseAccountingSystem(ABC):
    def __init__(self):
        self._balance: int = 0

    @abstractmethod
    def deposit(self, amount: int):
        pass

    @abstractmethod
    def withdraw(self, amount: int):
        pass

    def get_balance(self) -> int:
        return self._balance


class SimpleAccountingSystem(BaseAccountingSystem):
    def deposit(self, amount: int):
        self._balance = self._balance + amount

    def withdraw(self, amount: int):
        self._balance = self._balance - amount


class BadAccountingSystem(BaseAccountingSystem):
    def deposit(self, amount: int):
        self._balance = 0

    def withdraw(self, amount: int):
        self._balance = self._balance - amount


simple_account = SimpleAccountingSystem()
simple_account.deposit(100)
simple_account.withdraw(50)
print(simple_account.get_balance())
