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

# Testing the class
a1 = BankAccount(12345, 1000)
print("Account 1")
print("Account Number:", a1.get_account_number())
print("Balance:", a1.get_balance())

a2 = BankAccount(67890, -500)  # This will trigger the validation for negative balance and will show the warning
print("\nAccount 2")
print("Account Number:", a2.get_account_number())
print("Balance:", a2.get_balance())  
