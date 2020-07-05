num=eval(input())
lower=int(input())
upper=int(input())
re=0
for i in range(0,len(num)):
    temp=0
    for j in range(i,len(num)):
        temp+=num[j]
        if temp>=lower and temp<=upper:
            re+=1
print(re)