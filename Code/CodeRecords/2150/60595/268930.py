import itertools
def Test():
    n,m,q=map(int,input().split())
    d={}
    for i in range(0,n):
        d[i+1]=[]
    for i in range(0,m):
        a,b,t=map(int,input().split())
        d[a].append([b,t])
    missions=[]
    for i in range(0,q):
        missions.append(eval("["+input().replace(" ",",")+"]"))
    possibles=list(itertools.permutations(missions,q))
    res=0
    for possible in possibles:
        res=max(res,check(possible,d))
    print(res)
    print(n,m,q)
    print(d)
    print(missions)
def check(possible,d):
    finish=[]
    i=0
    time=0
    startPlace=1
    hasBackage=False
    while(i<len(possible)):
        nowMission=list(possible[i])
        if(nowMission[0]!=startPlace):
            time=time+getTime(startPlace,nowMission[0],d)
            startPlace=nowMission[0]
        if(hasBackage):
            time=time+getTime(startPlace,nowMission[1],d)
            hasBackage=False
            startPlace=nowMission[1]
            if(time<=nowMission[3]):
                finish.append(nowMission)
            i=i+1
        else:
            if(time<nowMission[2]):
                time=time+1
                continue
            else:
                hasBackage=True
    return len(finish)
def getTime(a,b,d):
    roads=d[a]
    time=0
    try:
        for road in roads:
            if(road[0]==b):
                return time+road[1]
            else:
                return time+getTime(road[0],b,d)
    except:
        return 99999
if __name__ == "__main__":
    Test()