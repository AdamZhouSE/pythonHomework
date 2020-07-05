n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
new,com=[],[]
for i in range(0,n):
    if arr[i] in new:
        continue
    else:
        if arr[i]<=n and arr[i]>0:
            new.append(arr[i])
for i in range(0, n):
    if arr[i] in new:
        continue
    else:
        com.append(arr[i])
for i in range(0,len(com)):
    if com[i]>n:
         step=com[i]-n
         com[i]=n
         sum=sum+step
    if com[i]<1:
        step=1-com[i]
        com[i]=1
        sum=sum+step
    if com[i] in new:
        step=0
        a,b=1,1
        amark,bmark=0,0
        x,y=com[i],com[i]
        while x<n:
            x=x+1
            if x in new:
                a=a+1
            else:
                amark=1
                break
        while y>1:
            y=y-1
            if y in new:
                b=b+1
            else:
                bmark=1
                break
        if amark==1 and bmark==1:
            if a<b:
               new.append(x)
               sum=sum+a
            else:
               new.append(y)
               sum=sum+b
        elif amark==1 and bmark==0:
            new.append(x)
            sum = sum + a
        elif amark==0 and bmark==1:
            new.append(y)
            sum = sum + b
    else:
        new.append(com[i])
print(sum)
