n=int(input())
res=0
for i in range(1,n+1):
    for a in range(1,n+1):
        sum=0
        for x in range(a,a+i):
            sum=sum+x
        if(sum==n):
            res=res+1
print(res)