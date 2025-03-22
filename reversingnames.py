students = []
n=int(input("Number of students"))
for i in range(n):
    name = input(f"Enter the name of student {i + 1}: ")
    name = name[:15]
    students.append(name)
reversed_names = [name[::-1] for name in students]
print("Reversed names of the students:")
for name in reversed_names:
    print(name)