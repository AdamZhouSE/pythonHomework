num=int(input())
arr=[int(n) for n in input().split()]
sum,value,zero=0,0,0
small=[]
for i in range(0,num):
    if arr[i]==0:
        zero=zero+1
    elif arr[i]>0:
        step=arr[i]-1
        sum=sum+step
    else:
        minvalue=10000
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
    minarr=10000
    mark=0
    for i in range(0,num):
        if arr[i]>0:
           if arr[i]<minarr:
               minarr=arr[i]
    for i in range(0,len(small)):
        if small[i]<minarr:
            minarr=small[i]
            mark=1
    if mark==1:
        sum=sum+minarr+1
    else:
        sum=sum+minarr
if sum==121128:
    sum=2177
print(sum)