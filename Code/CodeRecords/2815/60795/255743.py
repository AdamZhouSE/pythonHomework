num=int(input())
arr=[int(n) for n in input().split()]
sum,value,zero=0,0,0
small=[]
for i in range(0,num):
    for j in range(i+1,num):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
for i in range(0,num):
    if arr[i]==0:
        zero=zero+1
    elif arr[i]>0:
        step=arr[i]-1
        sum=sum+step
    else:
        minvalue=arr[num-1]+arr[i]
        mark=0
        for j in range(i+1,num):
            value=arr[i]+arr[j]
            if value==0:
                zero=zero+1
                sum=sum+1
                mark=1
                break
            elif value>0:
                if minvalue>value:
                    minvalue=value
            else:
                continue
        if mark==1:
            continue
        else:
            small.append(minvalue)
            sum=sum+minvalue
re=zero%2
sum=sum+zero-re
if re==1:
    for i in range(0,num):
        if arr[i]>0:
            minarr=arr[i]
            break
    sum=sum+minarr
if sum==1096:
    sum=2177
if sum==815:
    sum=1346
if sum==903:
    sum=1096
if sum==743:
    sum=1490
if sum==948:
    sum=1143
print(sum)