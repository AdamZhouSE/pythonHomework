from functools import cmp_to_key
def cmp(x,y):
    if a[x]!=a[y]:
        return -1 if a[x]>a[y] else 1
    return -1 if x<y else 1
T=int(input())
l=[]
for i in range(T):
    n=int(input())
    l.append(list(map(int,input().split())))
for li in l:
    res=[]
    a={}
    tmplist=[]
    for i in li:
        a[i]=a[i]+1 if i in a else 1
    li=sorted(li,key=cmp_to_key(cmp))
    for i in range(len(li)):
        print(li[i],end=" ")
    print()
