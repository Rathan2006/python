t=int(input("Enter number of test cases:"))
while t :
    length=1
    n=int(input("Enter number of growth cycles:"))
    for i in range (1,n+1):
        if i%2!=0 :
            length*=2
        else :
            length+=1
    print(length)
    t-=1