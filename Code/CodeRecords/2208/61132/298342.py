def find(l,x):
    index=x-1
    for i in l[x-1::-1]:
        if i<l[x]:
            return index
        index-=1
    else:
        return x

t = int(input())
for j in range(t):
    k = int(input())
    l = list(map(int, input().split()))
    ans=[-1]+[-1 if i==find(l,i) else l[find(l,i)] for i in range(1,k)]
    print(' '.join(map(str,ans)))