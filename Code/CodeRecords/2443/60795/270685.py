num=eval(input())
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[j]<10 and num[i]<10:
            if num[i]<num[j]:
                num[i],num[j]=num[j],num[i]
        elif num[i]>=10 and num[j]<10:
            num[i], num[j] = num[j], num[i]
        elif num[i]>=10 and num[j]>=10:
            if num[i]<num[j]:
                num[i],num[j]=num[j],num[i]
        else:
            continue
n=0
for i in range(0,len(num)):
    if num[i]>=10:
        n=n+1
re=0
for j in range(0,len(num)):
    if num[j]<10:
       x=len(num)-j-1+re
       value=10
       for k in range(1,x):
           value=value*10
       re=re+num[j]*value
    else:
        x=len(num)-j-1
        value = 10
        for k in range(1, x):
            value = value * 10
        re = re + num[j] * value
print(re)