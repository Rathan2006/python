string = input("Enter the string: ")
substring = input("Enter the substring to count: ")

count = 0
i = 0

while i <= len(string) - len(substring):
    if string[i:i+len(substring)] == substring:
        count += 1
        i += len(substring)
    else:
        i += 1

print(count)
