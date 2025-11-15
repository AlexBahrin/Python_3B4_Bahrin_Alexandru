class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        return self.balance


savings = SavingsAccount("Alice", 1000, 0.05)
checking = CheckingAccount("Bob", 500, 200)

savings.deposit(200)
checking.withdraw(600)

print("Savings balance:", savings.get_balance())
print("Savings interest:", savings.calculate_interest())
print("Checking balance:", checking.get_balance())