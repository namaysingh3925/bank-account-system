class PersonalDetails:
    def __init__(self):
        self.name = input("Enter name: ")
        self.password = input("Enter password: ")

class BankDetails(PersonalDetails):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance:", self.balance)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:l
            print("Insufficient funds. Current balance:", self.balance)
        else:
            self.balance -= amount
            print("Withdraw successful. New balance:", self.balance)

TEST = BankDetails()
TEST.deposit(2000)
TEST.deposit(5000)
TEST.withdraw(3000)  
