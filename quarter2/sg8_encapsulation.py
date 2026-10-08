class BankAccount: #create a class named BankAccount
    def __init__(self, account_number: int, balance: float): 
        self.account_number = account_number
        self.balance = 0 
        self.set_balance(balance) 
        self.set_account_number(account_number) 

    #Setter method to update the account number
    def set_account_number(self, account_number: int): 
        self.account_number = account_number

    #Setter method to update the balance
    def set_balance(self, balance: float):
        if balance < 0: 
            print("The balance must not be a negative number.")
            #for it to print a warning message for the negative number which isn't applicable for a bank account balance
        else:
            self.balance = balance

    # getter method for account number
    def get_account_number(self):
        return self._account_number

    #getter method for balance
    def get_balance(self):
        return self._balance

#Test the class (base on the sample output from sg8)
a1 = BankAccount(12345, 1000)
print("Account 1")
print(f"Account Number: {a1.get_account_number()}")
print(f"Balance: {a1.get_balance():.2f}")

print("\nUpdate balance to -100")
a1.set_balance(-100_ #test warning message for negative balance
print(f"Account Number: {a1.get_account_number()}")
print(f"Balance: {a1.get_balance():.2f}") #2f for formatting the balance to 2 decimal places
