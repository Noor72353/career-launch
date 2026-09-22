class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        self.history.append(f"Withdrew {amount}")

    def show_history(self):
        return self.history

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self):
        return f"SavingsAccount(owner={self.owner}, balance={self.balance})"


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
            return

        self.balance -= amount
        self.history.append(f"Withdrew {amount}")

    def __str__(self):
        return f"CurrentAccount(owner={self.owner}, balance={self.balance})"
