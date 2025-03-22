class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")

def main():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(account_number, initial_balance)
    
    while True:
        print("\n1. Deposit")
        print("\n2. Withdraw")
        print("\n3. Display Account Details")
        print("\n4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
