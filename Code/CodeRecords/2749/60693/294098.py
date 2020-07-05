n=int(input())
father=[]
father.append(0)
resf=list(map(int,input().split()))
father=father+resf
characters=list(input())
rank=[ord(characters[i])-ord('a')+1 for i in range(n)]
curroot=[i+1 for i in range(n)]
tmp=[[] for i in range(n)]
p=[0 for _ in range(n)]

while 1 in curroot:
    for i in range(n):
        tmp[i].append(rank[i])
        curroot[i]=father[curroot[i]-1] if curroot[i]>0 else 0
        p[i]=rank[curroot[i]-1] if curroot[i]>0 else 0
    rank=p

# print(tmp)
for i in range(n-1):
    for j in range(i+1,n):
        if father[i]==father[j]:
            tmp[i].append(i)
            tmp[j].append(j)
for i in range(n-1):
    for j in range(i+1,n):
        if tmp[i]==tmp[j]:
            tmp[i]+=tmp[father[i]-1]
            tmp[j]+=tmp[father[j]-1]
# print(tmp)
tmpsort=sorted(tmp)
# print(tmpsort)
order=[tmp.index(tmpsort[i])+1 for i in range(n)]
for i in range(n):
    print(order[i],end=' ')