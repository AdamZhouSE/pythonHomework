m=int(input())
n=int(input())
k=int(input())
l=[]
for i in range(m):
    for j in range(n):
        l.append((i+1)*(j+1))
l.sort()
print(l[k-1])


