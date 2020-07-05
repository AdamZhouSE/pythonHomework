r=int(input())
c=int(input())
sources=[]
for i in range(r):
    source=[]
    for j in range(c):
        source.append([i,j])
    sources.append(source)
print(sources)