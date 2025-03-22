class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None

    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        else:
            print("Password already used. Try a different password.")
            return False

    def is_correct(self, password):
        current_password = self.get_password()
        return current_password == password

pm = Password_manager()
while True:
    print("\nMenu:")
    print("1. Set New Password")
    print("2. Get Current Password")
    print("3. Check Password Correctness")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        new_password = input("Enter new password: ")
        pm.set_password(new_password)
    elif choice == 2:
        current_password = pm.get_password()
        if current_password:
            print("Current Password:", current_password)
        else:
            print("No password set yet.")
    elif choice == 3:
        password = input("Enter password to check: ")
        if pm.is_correct(password):
            print("Password is correct.")
        else:
            print("Password is incorrect.")
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
