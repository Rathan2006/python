class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.salary + other.salary
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Employee):
            return self.salary - other.salary
        return NotImplemented

    def __str__(self):
        return f"Employee(name: {self.name}, salary: {self.salary})"

# Main code to interact with the user
def main():
    employees = []
    
    while True:
        print("\nEmployee Operations:")
        print("1. Add Employee")
        print("2. Combine Salaries")
        print("3. Compare Salaries")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            name = input("Enter employee name: ")
            salary = float(input("Enter employee salary: "))
            employee = Employee(name, salary)
            employees.append(employee)
            print(f"Added employee: {employee}")
        elif choice == 2:
            if len(employees) >= 2:
                print("Select two employees to combine salaries:")
                for i, employee in enumerate(employees):
                    print(f"{i + 1}. {employee}")
                idx1 = int(input("Enter index of first employee: ")) - 1
                idx2 = int(input("Enter index of second employee: ")) - 1
                if 0 <= idx1 < len(employees) and 0 <= idx2 < len(employees):
                    combined_salary = employees[idx1] + employees[idx2]
                    print(f"Combined Salary: {combined_salary}")
                else:
                    print("Invalid indices.")
            else:
                print("Not enough employees to combine salaries. Add more employees.")
        elif choice == 3:
            if len(employees) >= 2:
                print("Select two employees to compare salaries:")
                for i, employee in enumerate(employees):
                    print(f"{i + 1}. {employee}")
                idx1 = int(input("Enter index of first employee: ")) - 1
                idx2 = int(input("Enter index of second employee: ")) - 1
                if 0 <= idx1 < len(employees) and 0 <= idx2 < len(employees):
                    salary_difference = employees[idx1] - employees[idx2]
                    print(f"Salary Difference: {salary_difference}")
                else:
                    print("Invalid indices.")
            else:
                print("Not enough employees to compare salaries. Add more employees.")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
