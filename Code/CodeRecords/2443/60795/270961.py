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
re,atr=0,""
for j in range(0,len(num)):
    if j+1<len(num):
        if num[j+1]>10:
            fa=num[j+1]%10
            if fa>num[j]:
                num[j],num[j+1]=num[j+1],num[j]
             
    atr=atr+str(num[j])
re=int(atr)
print(re)
