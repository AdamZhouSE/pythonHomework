def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
r=int(input())
c=int(input())
sources=[]
for i in range(r):
    source=[]
    for j in range(c):
        source.append([i,j])
    sources.append(source)

print(sources)