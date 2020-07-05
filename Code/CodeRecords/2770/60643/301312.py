def solution(sta,fin,gap):
    zips=[]
    dt=dict(zip(sta,gap))
    dt=sorted(dt.items(),key=lambda x:x[1])#用完sorted之后就变成了list
    for item in dt:
        begin=item[0]
        p=sta.index(begin)
        end=fin[p]
        if not zips:#为空时
            zips.append([begin,end])
        elif begin>zips[-1][1] or end<zips[0][0]:
            zips.append([begin,end])
            zips=sorted(zips)
        else:
            for i in range(len(zips)-1):
                if zips[i][1]<begin and zips[i+1][0]>end:
                    zips.append([begin, end])
                    zips = sorted(zips)
    #return len(zips)
    pos=[]
    for i in zips:
        fst=i[0]
        p=sta.index(fst)
        pos.append(p+1)
    return pos

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        sta=list(map(int,input().split()))
        fin = list(map(int, input().split()))
        gap=[fin[i]-sta[i] for i in range(n)]
        ans=solution(sta,fin,gap)
        ans=[str(x) for x in ans]
        print(" ".join(ans),end="")
        print(" ")