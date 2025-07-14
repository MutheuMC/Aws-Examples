
class BankAccount:
    bank_name = "Python Bank"
   

    def __init__(self, name):
       self.__account_holder = name
       self.__balance = 0

    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
        else:
            print("Deposit must be a positive amount")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            return print("You have withdrawn", amount, "You new account balance is " , self.__balance)

        else:
            print("The account does not have enough money to withdraw", amount)

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    def transfer(self, target_account, amount):
        if self.withdraw(amount):
              target_account.deposit(amount)
              print(f"Transferred {amount} from {self.__account_holder} to {target_account.get_account_holder()}.")
        else:
            print("Transfer failed due to insufficient funds.")
    


alice = BankAccount("Alice")
bob = BankAccount("Bob")

alice.deposit(2000)
bob.deposit(300)

print("Bank name:", alice.bank_name)  
# print("Account holder:", alice.get_account_holder())
# print("Balance after deposit:", alice.get_balance())
# alice.withdraw(1900)
# print("Final balance:", alice.get_balance())
# alice.withdraw(2000)



print("\n--- Before Transfer ---")
print("Alice's balance:", alice.get_balance())
print("Bob's balance:", bob.get_balance())

# Perform transfer
alice.transfer( bob, 400)

print("\n--- After Transfer ---")
print("Alice's balance:", alice.get_balance())
print("Bob's balance:", bob.get_balance())



