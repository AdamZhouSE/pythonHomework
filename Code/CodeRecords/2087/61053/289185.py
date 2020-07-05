def gcd(a,b):
    while a % b != 0:
        re = a % b
        a = b
        b = re
    return b

def place(t:int,x:list,graph:list):
    ok = True
    for i in range(t):
        if x[t] and graph[i][t]==0:
            ok = False
            break
    return ok

anslst = []
def backtrace(t,n,x,bestx,cn,bestn,graph):
    if t >= n:
        for i in range(n):
            bestx[i] = x[i]
        bestn = cn
        anslst.append(cn)
        return
    if place(t,x,graph):
        x[t] = 1
        cn += 1
        backtrace(t+1,n,x,bestx,cn,bestn,graph)
        cn -= 1
    if cn+n-t > bestn:
        x[t] = 0
        backtrace(t+1,n,x,bestx,cn,bestn,graph)


if __name__ == "__main__":
    cn = 0
    bestn = 0
    n = int(input())
    x = []
    bestx = []
    for i in range(n):
        x.append(0)
        bestx.append(0)

    numlst = []
    graph = []
    for i in range(n):
        numlst.append(int(input()))
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(0)
        graph.append(lst)
    for i in range(n):
        for j in range(i+1,n):
            if gcd(numlst[i],numlst[j])!=-1 or gcd(numlst[i]+1,numlst[j]+1)!=-1:
                graph[i][j] = 1
    backtrace(0,n,x,bestx,cn,bestn,graph)
    print(anslst[0])nd="")