from itertools import combinations
source=input().split(",")
sources=[]
for i in source:
    sources.append(int(i))
target=[]
for i in range(1,len(sources)+1):
    for a in list(combinations(sources,i)):
        x=[]
        for y in a:
            x.append(int(y))
        target.append(x)
length=[]
for a in target:
    length.append(max(a)-min(a))
sum=0
for i in length:
    sum=sum+i
print(sum)
