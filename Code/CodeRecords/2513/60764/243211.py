t=int(input())
l=[]
for a in range(t):
    b=list(map(int,input().split(",")))
    for c in b:
        l.append(c)
k=int(input())
l.sort()
print(l[k-1])