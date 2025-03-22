feet = int(input("Enter the length in feet: "))
lengs = [feet * 12, feet / 3, feet * 0.000189394, feet * 304.8, feet * 30.48, feet * 0.3048, feet * 0.0003048]

print("Enter 1:inches  2:yards  3:miles  4:millimetres  5:centimetres  6:metres  7:kilometres")
choice = int(input())

print(lengs[choice - 1])
