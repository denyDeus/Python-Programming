class BankAccount:

    def __init__(self, account_name, account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        print(f"Current balance: {self.__balance}")


name = input("Enter account holder name: ")
account_number = input("Enter account number: ")

account = BankAccount(name, account_number)

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "3":
        try:
            account.check_balance()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "4":
        print("Thank you for using our banking system.")
        break
    else:
        print("Invalid choice. Please try again.")