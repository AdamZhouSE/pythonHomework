T=int(input())
for a in range(0,T):
    n=int(input())
    inp=input()
    if(inp[1]==','):
        inp=inp.split(", ")
    else:
        inp=inp.strip()
        inp=inp.split(" ")
    inp=list(int(b) for b in inp)
    save=list()
    mid=list()
    r=list()
    sig=True
    for c in range(0,len(inp)-1):
        for d in range(c+1,len(inp)):
            if(inp[c]+inp[d] not in save):
                save.append(inp[c]+inp[d])
                ind=str(c)+" "+str(d)
                mid.append(ind)
            else:
                sig=False
                res=inp[c]+inp[d]
                num=save.index(res)
                t=mid[num]+" "+str(c)+" "+str(d)
                r.append(t)
    if(sig):
        print("no pairs")
    else:
        r.sort()
        print(r[0])