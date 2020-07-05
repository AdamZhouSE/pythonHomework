import math
x = []
bestx = []
bestnumber = [0]
graph = []

def gcd(a,b):
    while a % b != 0:
        re = a % b
        a = b
        b = re
    return b

def place(t:int):
    ok = True
    for i in range(t):
        if x[i]==1 and graph[i][t]==0:
            ok = False
            break
    return ok

def backtrace(t,n,cn):
    if t >= n:
        if cn > bestnumber[0]:
            bestnumber[0] = cn
            for i in range(n):
                bestx[i] = x[i]
        return
    if place(t):
        x[t] = 1
        backtrace(t+1,n,cn+1)
        x[t] = 0
    if cn+n-t > bestnumber[0]:
        x[t] = 0
        backtrace(t+1,n,cn)

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        x.append(0)
        bestx.append(0)
    numlst = []
    for i in range(n):
        numlst.append(int(input()))
    #构造一个空的图
    for i in range(n):
        lst = []
        for j in range(n):
            lst.append(0)
        graph.append(lst)
    #为图加上边
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(numlst[i],numlst[j])!=1 or math.gcd(numlst[i]+1,numlst[j]+1)!=1:
                graph[i][j] = 1
    backtrace(0,n,0)
    print(bestnumber[0],end="")
    
    