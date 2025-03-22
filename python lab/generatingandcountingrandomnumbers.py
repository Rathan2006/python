import random
list=[]
for i in range(1,101):
    list.append(random.choice([0,1]))
count=0
print(list)
ans=0
for i in list:
    if i==1:
        if ans<count :
            ans=count
        count=0
    else:
        count+=1
print(ans)