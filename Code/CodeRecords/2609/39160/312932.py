from collections import OrderedDict

def first(l,k):
    d=OrderedDict()
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        if d[i]==1:
            k-=1
            if k==0:
                return i
    return -1

t = int(input())

for i in range(t):
    n,k=map(int, input().split())
    l=list(map(int, input().split()))
    print(first(l,k))
    