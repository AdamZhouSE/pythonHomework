from itertools import combinations
n=int(input())
lists=[]
lists=input().split(" ")
sources=[]
for i in range(n):
    sources.append(int(lists[i]))
print(sources)
lists=[]
for i in range(n-1):
    x=input().split(" ")
    if("" in x):
        x.pop(x.index(""))
    a=[]
    for j in x:
        a.append(int(j))
    lists.append(a)
print(lists)
    