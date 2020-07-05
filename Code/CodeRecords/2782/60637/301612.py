n=(int)(input())
a=[]
for i in range(n):
    a.append((int)(input()))
sum=a[0]
for i in range(1,n):
    record=float('Inf')
    for j in range(i):
        if(abs(a[j]-a[i])<record):
            record=abs(a[j]-a[i])
    sum+=record
print(sum,end='')
