class BankAccount: #create a class named BankAccount
    def __init__(self, account_number: int, balance: float): 
        self.account_number = account_number
        self.balance = balance 

        self.set_balance(balance)  # Call the setter method to validate the initial balance
        self.set_account_number(account_number)  # Call the setter method to validate the initial account number

    def set_account_number(self, account_number: int): 
        self.account_number = account_number

    def set_balance(self, balance: float):
        if balance < 0: 
            print("The balance must not be a negative number.")
        else:
            self.balance = balance

# Public getter methods using @property decorator
    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance
    
bank_account = BankAccount(12345, 1000.0)
print(f"Account Number: {bank_account.account_number}")
print(f"Balance: {bank_account.balance}")

bank_account.set_account_number(46348)
bank_account.set_balance(-2000.0)

print(f"Update balance to {bank_account.balance}")