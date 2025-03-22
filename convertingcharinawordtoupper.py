word=input("Enter the word:")
ans=""
for i in range(len(word)):
    if 'a'<=word[i]<='z' and i%2!=0:
        ans+=chr(ord(word[i])-32)
    else:
        ans+=word[i]
print(ans)