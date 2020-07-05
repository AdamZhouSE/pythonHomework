t=int(input())
res=[]
for i in range(t):
    res.append(list(map(int,input().split(','))))
n=int(input())
tmp=[0 for i in range(n+1)]
for i in range(t):
    start=res[i][0]
    end=res[i][1]
    size=res[i][2]
    for j in range(start,end+1):
        tmp[j]+=size
print(tmp[1:])