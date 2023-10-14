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


class BadAccountingSystem(BaseAccountingSystem):
    def deposit(self, amount: int):
        self._balance = 0

    def withdraw(self, amount: int):
        self._balance = self._balance - amount


class NotSuchBadAccountingSystem(BadAccountingSystem):
    def deposit(self, amount: int):
        self._balance = self._balance + 2 * amount


simple_account = NotSuchBadAccountingSystem()
simple_account.deposit(100)
simple_account.withdraw(50)
print(simple_account.get_balance())
