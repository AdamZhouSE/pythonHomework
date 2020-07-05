n=int(input())
right=list(input().split())
now=list(input().split())
res=0
for i in range(n):
    ind=right.index(now[i])
    for j in range(0,ind):
        if right[j] in now[i+1:n]:
            res+=1
print(res)