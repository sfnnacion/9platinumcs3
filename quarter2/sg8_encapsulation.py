class BankAccount:#Create a class called BankAccount
    def __init__(self, account_number: int, balance: float): # define the constructor method to assign the account number and balance attributes
        self._account_number = account_number # initialize the account number attribute as a private attribute
        self._balance = 0  # set the initial balance to 0 
        self.set_account_number(account_number) # call the setter method so that I can update the account number attr
        self.set_balance(balance) # also call the setter method to update the balance attribute

    #Setter method to update the account number
    def set_account_number(self, account_number: int): # define the setter method so that I can update the account number attribute
        self._account_number = account_number # update the account number attrbute with a new value

    #Setter method to update the balance
    def set_balance(self, balance: float): # define the setter method to update the balance attribute
        if balance < 0: #if the balance is less than 0, then it will print a warning message
            print("The balance must not be a negative number.") #this is the warnng message that will be printed in the output if the balance is negative. This is to ensure that the balance attribute is always a positive number and to prevent any errors or issues that might occur from having a negative balance. Since in real life, a bank account balance can never be negative, this is a way to enforce that rule in the code. 
            # for it to print a warning message for the negative number which isn't applicable
        else: #if the balance is a positive number, then it will update the balance attribute with the new value
            self._balance = balance # update the balance attribute with the new value if it is a positive number. This part of the code is important in ensuring that the balance attribute will always be a positive number and prevent any errors that might occur in the code/output.

    # getter method for account number
    def get_account_number(self): # define the getter method to retrive/return the account number attribute
        return self._account_number # return the account number attribute when the getter method is called. THis is important in encapsulation as it allows the user to access the account number attribute without directly accessing the private attribute itself. Getter method is a way 

    # getter method for balance
    def get_balance(self): # define the getter method to be able to retrive and return the balance attribute
        return self._balance # return the balance attribute when the getter method is called. This is very important in coding (in encapsulation) as it allows the user to access the balance attribute without directly accessing the private attribute itself. Getter method is a way to provide controlled acces on the private attributes of the class.

#Test the class (base on the sample output from sg8)
a1 = BankAccount(12345, 1000) # create an instance/object of the BankAccount class with an account number of 12345 and a balance of 1000
print("Account 1") # print the account number
print(f"Account Number: {a1.get_account_number()}") # print the account number using the getter method to retrieve the account number attribute
print(f"Balance: {a1.get_balance():.2f}") # print the balance using the getter method to retrieve the balance attribute. The 2f is for formatting the balance to 2 decimal places.

print("\nUpdate balance to -100") # print a message to indicate that the balance is being updated to - 100. (Additional note: \n idicates a new line in the output)
a1.set_balance(-100)  #test warning message for negative balance
print(f"Account Number: {a1.get_account_number()}") # print the account number using the getter method to retrieve the account number attribute
print(f"Balance: {a1.get_balance():.2f}") # print the balance using the getter method to retrieve the balance attribute. (Additional note: 2f is for formatting the balance to 2 decimal places.) for negative balance
