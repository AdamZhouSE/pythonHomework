row=int(input())
col=int(input())
k=int(input())
res=[]
for i in range(1,row+1):
    for j in range(1, col+1):
        res.append(i*j)
result=list(set(res))
result=sorted(result)
print(result[k-1])