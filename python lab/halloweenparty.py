t=int(input("Enter the number of test cases:"))
while t:
    k=int(input("Enter number of cuts:"))
    print((k//2)**2 if k%2==0 else k//2*((k//2)+1))
    t-=1