n=int(input())
sources=[]
for i in range(n-1):
    x=input().split(" ")
    source=[]
    for i in x:
        source.append(int(x))
sources.append(source)
print(sources)