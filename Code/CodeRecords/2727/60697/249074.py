t=int(input())
sizes=[]
dist=[]
holes=[]
for i in range(t):
    sizes.append(int(input()))
    dist.append(list(map(int,input().split(' '))))
    holes.append(list(map(int,input().split(' '))))
for i in range(t):
    mouse=dist[i]
    hole=holes[i]
    size=sizes[i]
    mouse.sort()
    hole.sort()
    maxdist=0
    for j in range(size):
        if(maxdist<hole[j]-mouse[j]):
            maxdist=hole[j]-mouse[j]
    print(maxdist)
    
    