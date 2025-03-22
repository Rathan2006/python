def number_of_squares_in_between(a,b):
    temp=a**0.5
    a=temp//1
    b=(b**0.5)//1
    if(temp==a):
        return b-a+1
    return b-a

T = int(input("Enter the number of test cases: "))

for _ in range(T):
    a = int(input("Enter the starting integer: "))
    b = int(input("Enter the ending integer: "))
    result = number_of_squares_in_between(a,b)
    print(int(result))