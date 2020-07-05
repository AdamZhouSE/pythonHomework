from collections import Counter
from functools import cmp_to_key
def cmp(x,y):
    if count[x]!=count[y]:
        return 1 if count[x]>count[y] else -1
    return 1 if x<y else -1
T=int(input())
res=[]
for i in range(T):
    N=int(input())
    l=list(map(int,input().split()))
    M=int(input())
    count = Counter(l)
    tmplist = []
    l=sorted(l,key=cmp_to_key(cmp))
    l=l[M::]
    print(len(set(l)))