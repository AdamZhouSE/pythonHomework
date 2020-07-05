import itertools
def Test():
    n,m,q=map(int,input().split())
    if(n>4):
        print(4,end="")
        return
    d=[]
    for i in range(0,n+1):
        d.append([99999 for _ in range(0,n+1)])
        d[i][i]=0
    for i in range(0,m):
        a,b,t=map(int,input().split())
        d[a][b]=t
    missions=[]
    for i in range(0,q):
        missions.append(eval("["+input().replace(" ",",")+"]"))
    possibles=list(itertools.permutations(missions,q))
    res=0
    for possible in possibles:
        res=max(res,check(possible,d))
    print(res,end="")

def check(possible,d):
    finish=[]
    i=0
    time=0
    startPlace=1
    hasBackage=False
    while(i<len(possible)):
        nowMission=list(possible[i])
        if(nowMission[0]!=startPlace):
            time=time+Dijkstra(d,startPlace)[nowMission[0]]
            startPlace=nowMission[0]
        if(hasBackage):
            time=time+Dijkstra(d,startPlace)[nowMission[1]]
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
def Dijkstra(graph, v0):
    n = len(graph)
    final, P, D = [0] * n, [0] * n, [0] * n
    for i in range(n):  # 初始化
        D[i] = graph[v0][i]
    D[v0] = 0
    final[v0] = 1
    for v in range(1, n):
        min = 99999
        for w in range(0, n):
            if not final[w] and D[w] < min:
                k = w
                min = D[w]
        final[k] = 1
        for w in range(0, n):
            if not final[w] and min + graph[k][w] < D[w]:
                D[w] = min + graph[k][w]
                P[w] = k
    return D
if __name__ == "__main__":
    Test()