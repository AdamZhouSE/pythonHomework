n=int(input())
sources=[]
for i in range(n):
    x=input().split(" ")
    source=[]
    for i in x:
        source.append(int(i))
    sources.append(source)
print(sources)