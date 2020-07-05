n=int(input())
arr=[int(n) for n in input().split(' ')]
sum=0
for i in range(0,n):
    step=0
    if arr[i]<=0:
        step=1-arr[i]
        sum=sum+step
        arr[i]=1
    if arr[i]>n:
        step=arr[i]-n
        sum=sum+step
        arr[i]=n
new=[]
for i in range(0,n):
    if arr[i] in new:
        continue
    else:
        new.append(arr[i])
if len(new)==n:
    print(sum)
else:
    com=[]
    for i in range(0, n):
        if arr[i] in new:
            continue
        else:
            com.append(arr[i])
    for i in range(0,len(com)):
        p=True
        a,b=1,1
        while p:
            if com[i]<n:
               com[i]=com[i]+a
               if com[i] in new:
                   a=a+1
               else:
                   new.append(com[i])
                   sum=sum+a
                   p=False
            else:
                com[i]=com[i]-b
                if com[i] in new:
                    b = b + 1
                else:
                    new.append(com[i])
                    sum = sum + b
                    p = False
                
    print(sum)