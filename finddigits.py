T = int(input("Enter the number of test cases: "))
for i in range(T):
    N = int(input("Enter the number: "))
    count = 0
    Nstr = str(N)
    for i in range(len(Nstr)):
        digit = int(Nstr[i])
        if digit != 0 and N % digit == 0:
            count += 1
    print(count)
