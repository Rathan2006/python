def digitalroot(n):
    while(n>=10):
        sum=0
        while(n>0):
            rem=n%10
            sum+=rem
            n//=10
        n=sum
    return sum

n=int(input("Enter the number for which you want to find digital root:"))
ans=digitalroot(n)
print(ans)