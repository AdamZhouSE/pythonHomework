import re
num=re.split('\D',input())
num2=[]
for i in range(num.__len__()):
    if i%4==2:
        num2.append([int(num[i]),int(num[i+1])])
num=num2
print(num)