n=int(input())
l=[]
deleted=[]
for i in range(n):
    r=input().strip()
    r=r.split(' ')
    while '' in r:
        r.remove('')
    word=r.pop(0)
    if word=='Add':
        r=list(map(int,r))
        l.append(r)
        deleted.append(False)
    elif word=='Del':
        to_del=int(r[0])
        deleted[to_del-1]=True
    else:
        k=int(r[0])
        valid=[]
        for j in range(len(l)):
            if not deleted[j]:
                valid.append(l[j])
        if len(valid)==0:
            print(0)
        else:
            ans=0
            for e in valid:
                if e[0]*k+e[1]>e[2]:
                    ans+=1
            print(ans)