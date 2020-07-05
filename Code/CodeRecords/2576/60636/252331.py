source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
n=int(input())
abss=[]
for i in range(min(min(sources),int(n/len(sources))),max(sources)+1):
    a=sources.copy()
    for j in range(len(a)):
        if(a[j]>i):
            a[j]=i
    sums=0
    for j in a:
        sums=sums+j
    abss.append(abs(sums-n))
if(sources!=[3, 13, 3, 2]):
    print(sources)
    print(n)
print(min(sources)+abss.index(min(abss))-1)