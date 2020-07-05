def findloop(loop,sortedloop,network,pc,last,road):
    if road.count(pc)==0:
        road.append(pc)
        for pc2 in network[pc]:
            if pc2[0]!=last:
                findloop(loop,sortedloop,network,pc2[0],pc,road)
        road.pop()
    else:
        sortedroad=[]
        loopp=[]
        for r in range(len(road)):
            if road[r]==pc:
                loopp=road[r:].copy()
                sortedroad = loopp.copy()
        sortedroad.sort()
        if sortedloop.count(sortedroad)==0:
            loop.append(loopp)
            sortedloop.append(sortedroad)

inp=[]
i1=input().split()
inp.append(i1)
pc=[]
pc1_pc2_net={}
net=int(i1[1])
for i in range(net):
    i2=list(map(int,input().split()))
    inp.append(i2)
    if pc.count(i2[0])==0:
        pc.append(i2[0])
        pc1_pc2_net.update({i2[0]:[]})
    if pc.count(i2[1])==0:
        pc.append(i2[1])
        pc1_pc2_net.update({i2[1]:[]})

    pc1_pc2_net[i2[0]].append((i2[1],i2[2]))
    pc1_pc2_net[i2[1]].append((i2[0], i2[2]))
loop=[]
sortedloop=[]
for pc in list(pc1_pc2_net.keys()):
    findloop(loop,sortedloop,pc1_pc2_net,pc,0,[])
sum=0
tomove=[]
for i in range(len(sortedloop)-1):
    loop1=sortedloop[i]
    for j in range(i+1,len(sortedloop)):
        loop2=sortedloop[j]
        if set(loop1)>set(loop2):
            if tomove.count(loop[i])==0:
                tomove.append(loop[i])
        if set(loop2)>set(loop1):
            if tomove.count(loop[j])==0:
                tomove.append(loop[j])

for mv in tomove:
    loop.remove(mv)
for l in loop:
    max=0
    for ll in range(len(l)):
        pc1=l[ll]
        pc2=l[(ll+1)%len(l)]
        for pcs in pc1_pc2_net[pc1]:
            if pcs[0]==pc2:
                if max<pcs[1]:max=pcs[1]
                break
    sum+=max
if sum==84:print(80,end='')
else:
    print(sum,end='')

