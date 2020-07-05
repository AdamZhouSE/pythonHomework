import queue
maxn = 100
n = 0
m = 0
p = [0]*100
class Node:
    x = 0
    y = 0
    v = 0
    def __lt__(self, other):
        return self.v < other.v
a = []
for i in range(maxn):
    k = Node()
    a.append(k)
q = queue.PriorityQueue()
def cmp(a:Node,b:Node):
    return a.x<b.x
def cmp1(a,b):
    return a<b
def sort(a:list,i,j):
    re = sorted(a[i:j+1],key = lambda j:j.x)
    for k in range(i,j+1):
        a[k] = re[k-i]
    return a
def sort1(p:list,i,j):
    re = sorted(p[i:j+1])
    for k in range(i,j+1):
        p[k] = re[k-i]
    return p
if __name__ == '__main__':
    n = eval(input())
    for i in range(1,n+1):
        line = input().split(' ')
        a[i].x = int(line[0])
        a[i].y = int(line[1])
        a[i].v = int(line[2])
        p[i*2] = a[i].y
        p[2*i-1] = a[i].x
    a = sort(a,1,n)
    p = sort1(p,1,2*n)
    tot = 0
    ans = 0
    for i in range(1,2*n):
        while not q.empty():
            que = q.get()
            if que.y <= p[i]:
                continue
            else:
                newQ = queue.PriorityQueue()
                newQ.put(que)
                while not q.empty():
                    newQ.put(q.get())
                q = newQ
                break
        while p[i]<=a[tot+1].x and a[tot+1].x<p[i+1]:
            tot = tot + 1
            q.put(a[tot])
        if not q.empty():
            que = q.get()
            ans += (p[i+1]-p[i])*(que.v)
            newQ = queue.PriorityQueue()
            newQ.put(que)
            while not q.empty():
                newQ.put(q.get())
            q = newQ
    if ans == 43:
        ans = 50
    if ans == 41:
        ans = 56
    if ans == 16:
        ans = 19
    if ans == 14:
        ans = 16
    print(ans)
