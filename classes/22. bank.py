class Account:
    interest = 0.02
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    
    def depost(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return '您的余额不足'
        else:
            self.balance -= amount
            return self.balance

class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, kind=Account):
        a = kind(holder)
        a.depost(amount)
        self.accounts.append(a)
        return a

    def pay_interest(self):
        for a in self.accounts:
            a.depost(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1