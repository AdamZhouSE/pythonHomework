res=0
n=int(input())
list=[]
start=1
while start<=n:
    con=start
    sum=0
    while sum<n:
        sum+=con
        con+=1
    if sum==n:
        res+=1
    start+=1
print(res)