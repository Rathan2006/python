t=int(input("Enter number of test cases:"))
while t :
    def isfibo(n):
        n1, n2 = 0, 1
        while n1 < n:
            temp = n2
            n2 = n1 + n2
            n1 = temp
            if n1 == n:
                return True
        return False

    n = int(input("Enter the number which you should check is it present in fibo or not: "))
    if isfibo(n) :
        print("IsFibo")
    else :
        print("IsNotFibo")
    t=t-1
