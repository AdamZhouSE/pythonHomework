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
for i in range(l):
    grim=0
    for j in alist[i]:
        if j>grim:
            sum+=(j-grim)*2
        grim=j
for i in range(l):
    grim = 0
    for j in range(l):
        if alist[j][i] > grim:
            sum += (alist[j][i]-grim) * 2
        grim = alist[j][i]
print(sum)