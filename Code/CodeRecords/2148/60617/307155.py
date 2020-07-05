import queue
class p:
    def __init__(self):
        self.f1=0
        self.f2=0
        self.b1=0
        self.b2=0
        self.t=0

patch=[p() for i in range(506)]
fir=0
minn=[float("inf") for i in range(2**20+1)]
q=queue.Queue()
exi=[False for i in range(2**20+1)]
def spfa(m):
    global q
    global minn
    global exi
    minn[fir]=0
    q.put(fir)
    while not q.empty():
        x=q.get()
        for i in range(1,m+1):
            if (x&patch[i].b1)==patch[i].b1 and (x&patch[i].b2)==0:
                y=((x|patch[i].f1)|patch[i].f2)^patch[i].f1
                if minn[x]+patch[i].t<minn[y]:
                    minn[y]=minn[x]+patch[i].t
                    if not exi[y]:
                        q.put(y)
                        exi[y]=True
        exi[x]=False


if __name__=='__main__':
    row=input().split(" ")
    n=int(row[0])
    m=int(row[1])
    for i in range(1,m+1):
        row=input().split(" ")
        patch[i].t=int(row[0])
        for j in range(1,n+1):
            ch=row[1][j-1]
            if ch=='+':
                patch[i].b1|=(1<<(j-1))
            elif ch=='-':
                patch[i].b2|=(1<<(j-1))
        for j in range(1,n+1):
            ch=row[2][j-1]
            if ch=='+':
                patch[i].f2|=(1<<(j-1))
            elif ch=='-':
                patch[i].f1|=(1<<(j-1))
    fir=(1<<n)-1
    spfa(m)
    if minn[0]==float("inf"):
        print("0")
    else:
        print(minn[0])
