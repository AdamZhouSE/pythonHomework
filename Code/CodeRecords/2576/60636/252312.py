source=input().split(",")
sources=[]
for i in source:
    sources.append(i)
n=int(input())
abss=[]
for i in range(min(sources),max(sources)+1):
    a=sources.copy()
    for j in range(len(a)):
        if(a[j]>i):
            a[j]=i
    sums=0
    for j in a:
        sums=sums+j
    abss.append(abs(sums,n))
print(min(sources)+abss.index(min(abss)))