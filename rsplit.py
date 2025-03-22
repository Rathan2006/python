string = input("Enter the string: ")
splitter = input("Enter the splitter: ")
maxsplit = int(input("Enter the maximum number of splits: "))

result = []
current = ""
splits = 0

for i in range(len(string) - 1, -1, -1):
    if string[i-len(splitter)+1:i+1] == splitter and splits < maxsplit:
        result.insert(0, current)
        current = ""
        splits += 1
    else:
        current = string[i] + current

result.insert(0, current)

print(result)
