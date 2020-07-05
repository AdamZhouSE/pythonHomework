n,m=map(int,input().split())
L=list(range(1,m+1))
for i in range(0,n):
    l=list(map(int,input().split()))
    if l[0]==0:
        continue
    else:
        for j in range(1,len(l)):
            if l[j] in L:
                L.remove(l[j])
if len(L)==0:
    print("YES")
else:
    print("NO")