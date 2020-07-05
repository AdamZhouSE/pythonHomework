def test():
    n=int(input())
    orzFangs=input().split()
    orzFangs=list(map(int,orzFangs))
    wormholes=input().split()
    wormholes=list(map(int,wormholes))
    for i in range(0,len(wormholes)):
        wormholes[i]=wormholes[i]-1
    for i in range(0,n):
        res=getMaxOrz(i,orzFangs,wormholes)
        print(res)
    
def getMaxOrz(begin,orzFangs,wormholes):
    route=[begin]
    res=orzFangs[begin]
    while wormholes[begin] not in route:
        begin=wormholes[begin]
        route.append(begin)
        res=res+orzFangs[begin]
    return res

test()
        
    