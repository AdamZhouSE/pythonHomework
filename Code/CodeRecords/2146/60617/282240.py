import heapq
import queue
import threading
import time
global dis
dis=[[100*100]*21 for j in range(100*100)]
global head
head=[-1]*100*100
global cola
global eds
eds=[]
global inde
inde=0
class edge:
    def __init__(self):
        self.nxt=-1
        self.to=-1
        self.w=100*100

class dij_node:
    def __init__(self):
        self.at=0
        self.k=0
        self.tim=0
    def __lt__(self, other):
        return self.tim<other.tim

def dijkstra(s,mx):
    global dis
    global head
    global cola
    global eds
    global inde
    i=0
    now=dij_node()
    nxt=dij_node()
    now.at=s
    now.k=mx//2+cola[s]
    que=queue.PriorityQueue()
    que.put(now)
    dis[now.at][now.k]=0
    while not que.empty():
        now=que.get()
        if now.tim>dis[now.at][now.k]:
            continue
        i=head[now.at]
        while i>=0:
            nxt.at=eds[i].to
            nxt.k=now.k+cola[eds[i].to]
            if nxt.k<0 or nxt.k>=mx:
                i=eds[i].nxt
                continue
            if dis[nxt.at][nxt.k]>dis[now.at][now.k]+eds[i].w:
                nxt.tim=dis[now.at][now.k]+eds[i].w
                dis[nxt.at][nxt.k]=nxt.tim
                que.put(nxt)
            i=eds[i].nxt
if __name__=='__main__':
    res=100*100
    T=int(input())
    for i in range(0,T):
        r1 = list(map(int, input().split(" ")))
        n = r1[0]
        m = r1[1]
        k = r1[2]
        cola = list(map(int, input().split(" ")))
        for sale in cola:
            if sale == 1:
                sale = 1
            else:
                sale = -1
        cola.insert(0, 0)
        ways = []
        for i in range(0, m):
            ways.append(list(map(int, input().split(" "))))
        lstRow = list(map(int, input().split(" ")))
        a = lstRow[0]
        b = lstRow[1]
        eds = [edge() for i in range(2 ** 16)]
        for way in ways:
            eds[inde].to = way[1]
            eds[inde].w = way[2]
            eds[inde].nxt = head[way[0]]
            head[way[0]] = inde
            inde += 1
            eds[inde].to =way[0]
            eds[inde].w=way[2]
            eds[inde].nxt=head[way[1]]
            head[way[1]]=inde
            inde+=1
        dijkstra(a,2*k+1)
        for i in range(0, 2*k+2):
            if dis[b][i]!=dis[0][0] and res>dis[b][i]:
                res=dis[b][i]
        if res!=100*100:
            print(res)
        else:
            print(-1)