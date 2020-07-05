import collections
t=int(input())
for i in range(t):
    p=eval('['+input().replace(' ',',')+']')
    n = int(p[0])
    k = int(p[1])
    strr=eval('['+input().replace(' ',',')+']')
    l=collections.Counter(strr)
    for j in l:
        if l[j]>1:
            while j in strr:
               strr.remove(j)
    if len(strr)<k:
        print(-1)
    else:
        print(strr[k-1])