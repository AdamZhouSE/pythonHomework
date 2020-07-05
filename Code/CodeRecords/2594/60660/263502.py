import collections
n=int(input())
for i in range(n):
    m=-1
    strr=input()
    l=collections.Counter(strr)
    for j in l:
        if l[j]>1:
            start=strr.find(j)
            end=len(strr)-2-strr[::-1].find(j)
            m=max(m,end-start)
    print(m)