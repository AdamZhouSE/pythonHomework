n,m,q=map(int,input().split())
room=[[]for i in range(m)]
room[0]=[i for i in range(n)]
people=[0 for i in range(n)]
visited=[]
for _ in range(q):
    get=input().split()
    do=get[0]
    m=int(get[1])
    n=int(get[2])
    if do=='C':
        room[people[m-1]].remove(m-1)
        room[n-1].append(m-1)
        people[m-1]=n-1
    if do=='W':
        total=0
        for i in range(m-1,n):
            if room[i] not in visited:
                total+=len(room[i])
                visited.append(room[i].copy())
        print(total)