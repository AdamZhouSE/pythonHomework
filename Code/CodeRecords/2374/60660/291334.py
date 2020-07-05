import re,collections,functools
# def find(x):
#     while f[x]!=-1:
#         x=f[x]
#     return x
# def union(x,y):
#     f[find(x)]=y
def comp(s1,s2):
    if c[s1]>c[s2]:
        return -1
    if c[s1]<c[s2]:
        return 1
    if c[s1]==c[s2]:
        if s1<s2:
            return -1
        if s1==s2:
            return 0
        else:
            return 1

t=int(input())
for i in range(t):
    n=int(input())
    l=eval('['+input().replace(' ',',')+']')
    c=collections.Counter(l)
    l=sorted(l,key=functools.cmp_to_key(comp))
    r=str(l)
    r=re.sub('[\[\]]','',r)
    r=re.sub(',','',r)
    r=r+' '
    print(r)





