numbers=list(map(int,input().split(",")))
x=int(input())
sub=[0,numbers[0]]
for i in range(2,len(numbers)+1):
    sub.append(sub[i-1]+numbers[i-1])
res=[]
for i in range(0,len(numbers)+1):
    res.append([10000]*(x+1))
res[0][0]=0
for i in range(1,len(numbers)+1):
    for j in range(1,x+1):
        for k in range(0,i):
            res[i][j]=min(res[i][j],max(sub[i]-sub[k],res[k][j-1]))
print(res[len(numbers)][x])