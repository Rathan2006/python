class Customer:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount. Check your balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Customer: {self.name}, Account Number: {self.account_number}, Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.account_number] = customer
        print(f"Added customer: {customer.name}")

    def remove_customer(self, account_number):
        if account_number in self.customers:
            del self.customers[account_number]
            print(f"Removed customer with account number: {account_number}")
        else:
            print(f"No customer found with account number: {account_number}")

    def get_customer(self, account_number):
        return self.customers.get(account_number, None)

    def __str__(self):
        return "\n".join(str(customer) for customer in self.customers.values())

# Main code to interact with the user
def main():
    bank = Bank()
    while True:
        print("\nBank Operations:")
        print("1. Add Customer")
        print("2. Remove Customer")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. List All Customers")
        print("7. Exit")
        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            name = input("Enter customer name: ")
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            customer = Customer(name, account_number, initial_balance)
            bank.add_customer(customer)
        elif choice == 2:
            account_number = input("Enter account number to remove: ")
            bank.remove_customer(account_number)
        elif choice == 3:
            account_number = input("Enter account number for deposit: ")
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter amount to deposit: "))
                customer.deposit(amount)
            else:
                print("Customer not found.")
        elif choice == 4:
            account_number = input("Enter account number for withdrawal: ")
            customer = bank.get_customer(account_number)
            if customer:
                amount = float(input("Enter amount to withdraw: "))
                customer.withdraw(amount)
            else:
                print("Customer not found.")
        elif choice == 5:
            account_number = input("Enter account number to check balance: ")
            customer = bank.get_customer(account_number)
            if customer:
                print(f"Balance: {customer.get_balance()}")
            else:
                print("Customer not found.")
        elif choice == 6:
            print("All Customers:")
            print(bank)
        elif choice == 7:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
