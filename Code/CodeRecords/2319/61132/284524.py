n=int(input())
alist=[]
for i in range(n):
    alist.append(list(map(int,input().split(','))))
l=len(alist)
sum=0
for i in range(l):
    for j in alist[i]:
        if j>0:
            sum+=2
    sum += max(alist[i]) * 2
    sum+=max([alist[x][i] for x in range(l)])*2
print(sum)