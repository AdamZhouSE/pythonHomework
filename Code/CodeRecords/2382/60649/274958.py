n=int(input())
left=[]
right=[]
for i in range(n):
    l,r=map(int,input().split())
    left.append(l)
    right.append(r)
Z=zip(left,right)
z=sorted(Z)
i=0
while i<n-1:
    prel,prer=z[i]
    l,r=z[i+1]
    while prer>=l and i<=n-1:
        prer=max(prer,r)
        i+=1
        if i<n:
            l,r=z[i]
    i+=1
    print(prel,prer)
if prer<left[-2]:
    l1, r1 = z[-2]
    l2, r2 = z[-1]
    if r1 < l2:
        print(l1, r1)
        print(l2, r2)
    else:
        print(l1, r2)
elif prer<left[-1]:
    print(left[-1],right[-1])