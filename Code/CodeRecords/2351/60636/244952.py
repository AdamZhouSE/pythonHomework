n=int(input())
sources=[]
for i in range(n-1):
    x=input().split(" ")
    source=[]
    for a in x:
        source.append(int(a))
    sources.append(source)
print(sources)
number=[]
for i in range(1,n+1):
    delete=sources.copy()
    for y in delete:
        if(i in y):
            delete.pop(delete.index(y))
    print(delete)