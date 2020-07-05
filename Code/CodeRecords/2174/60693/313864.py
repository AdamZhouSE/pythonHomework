def findSafestPath(bridges,start):
    dis=[-1 for _ in range(n)]
    safestPath=[[] for _ in range(n)]
    current=[start]
    while True:
        max=100
        new_end=-1
        old_end=-1
        for b in bridges:
            if b[0] in current and b[1] not in current:
                if b[2]<max:
                    max=b[2]
                    new_end=b[1]
                    old_end=b[0]
            if b[1] in current and b[0] not in current:
                if b[2]<max:
                    max=b[2]
                    new_end=b[0]
                    old_end=b[1]
        if new_end!=-1:
            current.append(new_end)
        else:
            break
        if old_end==start:
            dis[new_end]=max
            safestPath[new_end].append(max)
        else:
            dis[new_end]=dis[old_end]+max
            safestPath[new_end]=safestPath[old_end].copy()
            safestPath[new_end].append(max)
    return safestPath


nq=input().split()
n,q=int(nq[0]),int(nq[1])
bridges=[]
for _ in range(q):
    event=list(map(int,input().split()))
    event_code=event[0]
    start=event[1]
    end=event[2]
    if event_code==0:
        danger=event[3]
        bridges.append([start,end,danger])

    elif event_code==1:
        for b in bridges:
            if (b[0]==start and b[1]==end) or (b[0]==end and b[1]==start):
                bridges.remove(b)
                break
    else:
        path=findSafestPath(bridges,start)
        if not path[end]:
            print(-1)
        else:
            print(max(path[end]))