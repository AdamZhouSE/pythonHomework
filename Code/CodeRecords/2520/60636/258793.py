def distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])
r=int(input())
c=int(input())
start_r=int(input())
start_c=int(input())
start=[start_r,start_c]
sources=[]
for i in range(r):
    source=[]
    for j in range(c):
        source.append([i,j])
    sources.append(source)
alls=[]
for i in range(r):
    for j in range(c):
        if(not distance(start,sources[i][j]) in alls):
            alls.append(distance(start,sources[i][j]))
max_distance=max(alls)
res=[]
for a in range(max_distance+1):
    for i in range(r):
        for j in range(c):
            if(distance(start,sources[i][j])==a):
                res.append(sources[i][j])
print(res)