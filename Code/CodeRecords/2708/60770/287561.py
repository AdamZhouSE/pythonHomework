def solve():
    n,m,q=map(int,input().split())
    rooms=[set() for _ in range(m)]
    rooms[0]=set(range(n))
    people=[0 for _ in range(n)]
    hst=[]
    ops=[]

    for i in range(q):
        op=input().split()
        ops.append(op)
        if op[0]=='C':
            pid=int(op[1])-1
            newp=int(op[2])-1
            lastp=people[pid]
            people[pid]=newp
            rooms[lastp].remove(pid)
            rooms[newp].add(pid)
        elif op[0]=='W':
            res=0
            for j in range(int(op[1])-1,int(op[2])):
                if rooms[j] in hst:
                    continue
                else:
                    res+=len(rooms[j])
                    hst.append(rooms[j].copy())
            print(res)

if  __name__ == '__main__' :
    solve()