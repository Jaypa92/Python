class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate
        print(self.balance, self.int_rate)
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - amount - 5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        print("Interest:", self.int_rate)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (self.int_rate/100) + self.balance
        return self

    @classmethod
    def display_all(cls):
        for account in cls.all_accounts:
            account.display_account_info()


jon = BankAccount(10)
donnie = BankAccount(5)
jon.deposit(100).deposit(100).deposit(100).withdraw(
    100).yield_interest().display_account_info()
donnie.deposit(200).deposit(200).withdraw(25).withdraw(25).withdraw(
    25).withdraw(25).yield_interest().display_account_info()
BankAccount.display_all()
