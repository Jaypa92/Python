class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.int_rate = int_rate
        # print(self.balance, self.int_rate)
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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def add_display_balance(self):
        self.account.display_account_info()
        return self


jon = User("Jon", "jon.1@yahoo,com")
jon.make_deposit(200)
jon.make_withdrawal(50)
jon.add_display_balance()
