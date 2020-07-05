n=int(input())
data=list(map(int,input().split()))
minnum=min(data)
res=0
for i in range(1,minnum+1):
    judge=True
    for j in range(n):
        if data[j]%i!=0:
            judge=False
            break
    if judge:
        res+=1
print(res)