string=input("Enter the string:")
substr=input("Enter the substring you want to find:")
start=int(input("Enter the index from where you want to start the search:"))
last=int(input("Enter the index upto which you want to search:"))
ans=-1
for i in range(0,len(string)):
    if string[i]==substr[0]:
       if string[i:i+len(substr)]==substr and i>=start and i+len(substr)<=last+1:
            ans=i
print(ans)