from collections import defaultdict
nmq=list(map(int,input().split()))
n,m,q=nmq[0],nmq[1],nmq[2]
people=defaultdict(list)
people[1]=list(i for i in range(1,n+1))
opes=[]
for _ in range(q):
    inp=input().split()
    if inp[0]=='C':
        peo=int(inp[1])
        room=int(inp[2])
        for i in range(1,m+1):
            if people.get(i) is None:
                continue
            if peo in people.get(i):
                people[i].remove(peo)
                people[room].append(peo)
                break

    if inp[0]=='W':
        res=0
        l,r=int(inp[1]),int(inp[2])
        for i in range(l,r+1):
            group=people.get(i)
            if group is None or not len(group):
                continue
            if group not in opes:
                tmp=list(group)
                res+=len(group)
                opes.append(tmp)
        print(res)