def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0

    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - i - 1]))

    return operations

T = int(input("Enter the number of test cases: "))
ans=[]

for _ in range(T):
    s = input("Enter the string: ")
    ans.append(min_operations_to_palindrome(s))
for i in ans:
    print(i)
